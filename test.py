import time
# Import xboxControlleren
import xbox

# Import the PCA9685 module. https://github.com/adafruit/Adafruit_Python_PCA9685/
import Adafruit_PCA9685

# Configure min and max servo pulse lengths
servo_min = 125  # Min pulse length out of 4096
servo_max = 625  # Max pulse length out of 4096

pwm = Adafruit_PCA9685.PCA9685()
pwm.set_pwm_freq(60)

joy = xbox.Joystick()

while not joy.Back():
    (x,y) = joy.leftStick()
    if (x != 0) or (y != 0):
        #print("leftX: " + str(joy.leftX()))
        #print("leftY: " + str(joy.leftY()))
        #time.sleep(0.2)
        pwm.set_pwm(0, 0, int(375+(x*225)))
        print(375+(x*250))
        time.sleep(0.1)