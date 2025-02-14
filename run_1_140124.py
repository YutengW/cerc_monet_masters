from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch, run_task, multitask

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
# Code for the Missions
#------------------------------------------

#----------------------------------
#Masterpiece,Expert,Audience Member
#----------------------------------

#Drive the robot to drop the art piece and museum director
drive_base.straight(407) #start from home area
#Reduce the turn speed to improve accuracy
drive_base.settings(turn_rate=80,turn_acceleration=300)
drive_base.turn(-57) # slow turn towards museum area
drive_base.straight(900) #drop Anna,Masterpiece, one audience member

#---------------------------------
#M11 light show
#---------------------------------

drive_base.turn(-32) # turn towards light show
drive_base.straight(-180) # drive backwards to light show
#back_motor.run_angle(500,-1650)
#Define a function to run back and front motor simultaneously

async def front_and_back():
    await multitask(back_motor.run_angle(500,-1650),front_motor.run_angle(400,-250))                                                    
run_task(front_and_back())  #spin light show and front arm moves down

#---------------------------------
# M05, Augmented reality statue
#---------------------------------

drive_base.straight(75) #drive forward a little  
drive_base.turn(43) # turn towards M05
drive_base.straight(175) #drive towards M05
# increase the turn speed and acceleration settings
drive_base.settings(turn_rate=202,turn_acceleration=910)                      
drive_base.turn(87) #turn the base quickly to open the statue

#---------------------------------
# M03 - Immersive Experience
#---------------------------------

drive_base.straight(140) #move forwards a bit
drive_base.turn(137) # turn towards M03 direction
# Define a function to Move forward and raise the front arm simultaneously  
####
async def forward_and_raise_arm():
    await multitask(front_motor.run_angle(400,250),drive_base.straight(400))
run_task(forward_and_raise_arm())  #move forward while raising the arm up

drive_base.turn(90)  #turn the front of the robot to M03
drive_base.straight(15)  #drive forward a little
front_motor.run_angle(400,-250) # push immersive experience down
wait(300) 
front_motor.run_angle(400,250) #lift arm up

#---------------------------------
#Go Home 
#---------------------------------

#increase the speed to save time while heading back to home area
drive_base.settings(straight_speed=600,straight_acceleration=1200)
drive_base.curve(-600,-110,Stop.COAST) # come back in a curve 


