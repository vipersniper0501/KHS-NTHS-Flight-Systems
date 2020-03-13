import asyncio
import serial

# import serial_asyncio

filepath = "/home/pi/Mamdau2DATA/geigerCounterOutput.txt"


# https://www.raspberrypi.org/documentation/linux/usage/systemd.md

# class output(asyncio.Protocol):
#    def connection_made(self, transport):
#        self.transport = transport
#        print('port opened', transport)
#        transport.serial.rts = False
#        transport.write(b'testing testing\n')
#
#    def data_received(self, data):
#        print('data recieved', repr(data))
#        self.transport.close()
#
#    def connection_lost(self, exc):
#        print('Port Closed')
#        asyncio.get_event_loop().stop()


async def read_in(queue):
    buffer = bytearray()
    ser = serial.Serial(port='/dev/ttyAMA0', timeout=0, exclusive=True)
    while True:
        raw = bytearray(1024)
        try:
            if not ser.is_open:  # if port not open (due to not connecting correctly and not staying connected), reopens port
                buffer = bytearray()
                ser.open()  # opens port
                print('Reopened Serial Port')
            bytes_read = ser.readinto(raw)
            raw = ser.readline(bytes_read)
            print(bytes_read, raw)
            buffer += raw[:bytes_read]
            if b'\n' in buffer:
                print('FOUND NEW LINE')
                i = buffer.index(b'\n')
                data = str(buffer[:i])
                data, _, buffer = buffer.partition(b'\n')
                await queue.put(data)
                print(data)
                buffer = buffer[i:]
                await asyncio.sleep(1)
        except serial.SerialException as e:
            ser.close()
            print('Error:')
            print(e)
            await asyncio.sleep(1)
        await asyncio.sleep(.001)
# READS Serial Connection and manages connection


async def process(in_q, out_q):
    while True:
        item = await in_q.get()
        # print('process', item)
        await out_q.put(item)
        # adds timestamp


async def print_out(queue):
    with open(filepath, 'wb+') as f:
        while True:
            data = await queue.get()
            print(data)
            f.write(data)
            print('Wrote Data')
            # prints out to file


def main():
    in_q = asyncio.Queue(maxsize=100)
    out_q = asyncio.Queue()
    loop = asyncio.get_event_loop()
    #    coro = serial_asyncio.create_serial_connection(loop,Output, 'dev/ttyAMA0')
    #    loop.create_task(coro)
    loop.create_task(read_in(in_q))
    loop.create_task(process(in_q, out_q))
    loop.create_task(print_out(out_q))
    loop.run_forever()


if __name__ == '__main__':
    main()
