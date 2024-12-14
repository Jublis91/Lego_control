from pybricks.hubs import TechnicHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = TechnicHub()

motor_left = Motor(Port.A)
motor_right = Motor(Port.B)

# 1600 seems to be the max ??
motor_left.run(1600) # Run the motor left at 1600 degrees/s speed. Forward
print(f"Motor A is running{motor_left.speed()}")
motor_right.run(-1600) # Run the motor right at 1600 degrees/s speed. Forward
print(f"Motor B is running{motor_right.speed()}")

wait(2000)

motor_left.stop() # Stop the motor left.
print(f"Motor A is stopped{motor_left.speed()}")
motor_right.stop() # Stop the motor right.
print(f"Motor B is stopped{motor_right.speed()}")