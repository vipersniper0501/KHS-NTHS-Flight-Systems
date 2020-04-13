import asyncio
import datetime
import pathlib

BASE_PATH = '/sys/bus/w1/devices'
OUTPUT_PATH = '/home/pi/Mamdau2DATA/TempDATA.csv'
# BASE_PATH = '.'
# OUTPUT_PATH = 'temp_out.txt'


def main():
    devices = pathlib.Path(BASE_PATH).glob('28-*/w1_slave')
    queue = asyncio.Queue()
    loop = asyncio.get_event_loop()
    for device in devices:
        loop.create_task(read_sensor(queue, device))
    loop.create_task(write_data(queue))
    loop.run_forever()


async def read_sensor(queue, device):
    while True:
        with open(device) as f:
            lines = f.readlines()
        if has_successful_reading(lines):
            _, _, temp_raw = lines[1].rpartition('t=')
            await queue.put((device.parent.name, temp_raw))
        await asyncio.sleep(0.2)


def has_successful_reading(lines):
    if len(lines) < 2:
        return False
    return lines[0].strip()[-3:] == 'YES' and 't=' in lines[1]


async def write_data(queue):
    with open(OUTPUT_PATH, 'w+') as f:
        while True:
            device, temp_raw = await queue.get()
            try:
                temp_celsius = float(temp_raw) / 1000.0
            except ValueError:
                continue
            timestamp = datetime.datetime.now(tz=datetime.timezone.utc).isoformat()
            f.write(f'{timestamp}, {device}, {temp_celsius:0.2f}\n')
            print(f'{timestamp} {device} {temp_celsius:0.2f}')
            f.flush()


if __name__ == '__main__':
    main()
