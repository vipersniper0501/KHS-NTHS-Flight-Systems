import asyncio
import datetime
import serial

filepath = "/home/pi/Mamdau2DATA/geigerCounterOutput.csv"


# https://www.raspberrypi.org/documentation/linux/usage/systemd.md

# This Geiger Counter measures Beta and Gamma radiation in micro-Sieverts or "uSv"
# The Geiger Counter measures the Counts per Second (CPS), Counts per Minute (CPM), and uSv/hr (Counts per Hour)

# Basic description of how code works:
# The program creates three threads for three different functions
# The first thread (read_in) only takes the raw data from the geiger counter and keeps the connection alive between the Pi and the Geiger Counter. The raw data that this thread collects will given to the second thread.
# The second thread (time_stamp) adds a time stamp to the beginning of the geiger counter output that was captured by the first thread so the Science Team can know when the data was captured. Once that time stamp is added, the new data is given to the third thread.
# The third and final thread (print_out) takes the data from the second thread and places it into a spreadsheet.
#
# These are all running in different asynchronus threads because if they were not then the code would only be working on one line of data at a time making the program extremely slow.

async def read_in(queue):
    buffer = bytearray()
    ser = serial.Serial(port='/dev/ttyAMA0', timeout=0, exclusive=True) 
    while True:
        try:
            if not ser.is_open:  # if port not open (due to not connecting correctly and not staying connected), reopens port
                buffer = bytearray()
                ser.open()  # opens port
                print('Reopened Serial Port')
            raw = ser.read(1024)
            buffer += raw
            if b'\n' in buffer:
                print('FOUND NEW LINE')
                print('   buffer ', buffer)
                data, _, buffer = buffer.partition(b'\n')
                print('   record ', data)
                print('    extra ', buffer)
                data = data.decode('utf-8')
                await queue.put(data)
        except serial.SerialException as e:
            ser.close()
            print('Error:', e)
            await asyncio.sleep(1)
        await asyncio.sleep(.001)
# READS Serial Connection and manages connection


async def time_stamp(in_q, out_q):
    while True:
        item = await in_q.get()
        stamped = '{} {}'.format(datetime.datetime.now(tz=datetime.timezone.utc).isoformat(), item)
        await out_q.put(stamped)


async def print_out(queue):
    with open(filepath, 'a') as f:
        while True:
            data = await queue.get()
            print('output ', data)
            f.write(data + '\n')
            f.flush()


def main():
    in_q = asyncio.Queue()
    out_q = asyncio.Queue()
    loop = asyncio.get_event_loop()
    loop.create_task(read_in(in_q))
    loop.create_task(time_stamp(in_q, out_q))
    loop.create_task(print_out(out_q))
    loop.run_forever()


if __name__ == '__main__':
    main()
