import time
from machine import Pin, PWM
from machine import UART, Pin
import time
from myfunctions import getdistance

uart1 = UART(1, baudrate=115200, tx=Pin(8), rx=Pin(9))  # initialize uart pins
#
# setting tfmini to default mode
default = [0x42, 0x57, 0x02, 0x00, 0x00, 0x00, 0x01, 0x06]  # default
# default = [0x42, 0x57, 0x02, 0x00, 0x00, 0x00, 0x04, 0x06] #string output
default = bytearray(default)
uart1.write(default)  # setting tfmini to default mode
time.sleep(0.1)

# connection : brown: ground
# orange: 5V
# yellow: PWM
panservo = PWM(Pin(6))  # pan servo PWM connect to GP6
tiltservo = PWM(Pin(7))  # tilt servo PWM connect to GP7
panservo.freq(50)
tiltservo.freq(50)
'''duty cycle values:
Min : 0.98ms
Mid : 1.64ms
Max : 2.3ms
The code will run the entire range of the servos in 100 steps
'''
file = open("distance.txt", "w")

# write to text file
tilt_duty = 995000  # ns
while tilt_duty <= 2300000:  # ns
    tiltservo.duty_ns(tilt_duty)
    time.sleep(0.05)
    tilt_duty = tilt_duty + 13050  # ns
    print("tilt_duty = ", tilt_duty)
    pan_duty = 995000  # ns
    panservo.duty_ns(pan_duty)
    time.sleep(1)

    while pan_duty <= 2300000:  # ns
        panservo.duty_ns(pan_duty)
        time.sleep(0.05)
        distance = getdistance(uart1)
        while distance>12:
            distance=getdistance(uart1)
        file.write(str(distance))
        file.write("\n")
        print("distance = ", distance)
        print("pan_duty = ", pan_duty)
        pan_duty = pan_duty + 13050  # ns
file.close()



