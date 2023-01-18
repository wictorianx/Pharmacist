import serial
import time
# # Serial port parameters
serial_speed = 9600
serial_port = '/dev/tty.HC-06' # bluetooth shield hc-06



print ("conecting to serial port ...")
ser = serial.Serial(port=serial_port, baudrate=serial_speed, timeout=1)
print ("sending message to turn on PIN 13 ...")
# # ser.flushInput()
# ser.write(bytes("x",encoding="ascii"))

# print ("recieving message from arduino ...")
# data = ser.readline()
for i in range(10000000000000000000000):
    ser.write(str("0").encode("ascii"))
data=""
if (data != ""):
    print ("arduino says: %s" % data)
else:
    print ("arduino doesnt respond")

time.sleep(4)
print ("finish program and close connection!")