from pybricks.hubs import TechnicHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = TechnicHub()

motor_cent = Motor(Port.C)


# 1600 seems to be the max ??
motor_cent.run(-1600) # Run the motor left at 1600 degrees/s speed. Left
print(f"Motor A is running{motor_left.speed()}")
motor_cent.run(1600) # Run the motor right at 1600 degrees/s speed. Right
print(f"Motor B is running{motor_right.speed()}")

wait(2000)

motor_cent.stop() # Stop the motor left.
print(f"Motor A is stopped{motor_left.speed()}")
