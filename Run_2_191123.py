from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch, hub_menu, multitask, run_task

hub = PrimeHub()
#Initialisate the robot 
# Step 1 - Initialize the drive base 
# Step 2 - Initialize the front and back motors 
# Step 3 - Initialize the left and right color sensors in the front
#---------------------------------------------------------------------

# Initialize both motors. In this example, the motor on the
# left must turn counterclockwise to make the robot go forward.
left_motor = Motor(Port.B, Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.A)

# Initialize the drive base. 
# In our robot, the wheel diameter is 88mm.
# The distance between the two wheel-ground contact points is 145mm.
drive_base = DriveBase(left_motor, right_motor, wheel_diameter=88, axle_track=145)
# Optionally, uncomment the line below to use the gyro for improved accuracy.
drive_base.use_gyro(True)

#Initialize the front abnd back motors 
front_motor = Motor(Port.D)
back_motor = Motor(Port.C)

# Initialize the color sensors.
right_sensor = ColorSensor(Port.F)
left_sensor = ColorSensor(Port.E)


#------------------------------------------
# Code for the robot
#-----------------------------------------
#move for 10cm
drive_base.straight(110)
#turn right 42 degrees
drive_base.turn(48)
#move straight for 20cm
drive_base.straight(385)

front_motor.run_angle(300,120)
drive_base.straight(10)
front_motor.run_angle(300,120)
drive_base.straight(10)
front_motor.run_angle(300,120)
drive_base.straight(10)

drive_base.turn(20)
wait(1200)
drive_base.turn(25)
drive_base.straight(400)
drive_base.turn(85)
drive_base.straight(160)
front_motor.run_angle(300,-300)
drive_base.straight(-70)
front_motor.run_angle(300,300)
