import pygame
from pybricks.hubs import TechnicHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Port

# Yhdistä ensimmäinen Technic Hub
hub_upper = TechnicHub()
motor1 = Motor(Port.A)  # Hub 1, moottori Port.A
motor2 = Motor(Port.B)  # Hub 1, moottori Port.B
motor3 = Motor(Port.C)  # Hub 1, moottori Port.C
motor4 = Motor(Port.D)  # Hub 1, moottori Port.D

# Yhdistä toinen Technic Hub
hub_lower = TechnicHub()
motor5 = Motor(Port.A)  # Hub 2, moottori Port.A
motor6 = Motor(Port.B)  # Hub 2, moottori Port.B
motor7 = Motor(Port.C)  # Hub 2, moottori Port.C

# Alusta Xbox-ohjain Pygamella
pygame.init()
pygame.joystick.init()

joystick = pygame.joystick.Joystick(0)  # 0 = ensimmäinen ohjain
joystick.init()

print(f"Connected to joystick: {joystick.get_name()}")

button_names = {
    0: "A",
    1: "B",
    2: "X",
    3: "Y",
    4: "LB",
    5: "RB",
    6: "Back",
    7: "Start",
    8: "L3",
    9: "R3",
    10: "D-pad Up",
    11: "D-pad Down",
    12: "D-pad Left",
    13: "D-pad Right",
    14: "left trigger",
    15: "right trigger",
    16: "left stick x-axis",
    17: "left stick y-axis",
    18: "right stick x-axis",
    19: "right stick y-axis"
}

# Funktio moottorin nopeuden ohjaamiseen
def run_motor(motor, speed):
    motor.run(speed)

# Pysäytä moottori
def stop_motor(motor):
    motor.stop()  # Poistettiin Stop.BRAKE, koska se ei ole tarpeen

try:
    while True:
        pygame.event.pump()  # Päivitä tapahtumajono

        # 1. Käytä painikkeita moottorin toimintaan
        if joystick.get_button(0):  # A-nappi
            run_motor(motor5, 500)  # Käynnistä moottori 1 nopeudella 500 deg/s
            print("Motor 1 running forward!")
        elif joystick.get_button(1):  # B-nappi
            run_motor(motor5, -500)  # Käynnistä moottori 1 taaksepäin nopeudella -500 deg/s
            print("Motor 1 running backward!")
        elif joystick.get_button(2):  # X-nappi
            stop_motor(motor5)  # Pysäytä moottori 1
            print("Motor 1 stopped.")

        # 2. Käytä triggereitä nopeuden ohjaukseen
        trigger_left = joystick.get_axis(2)  # LT (Vasen liipaisin)
        trigger_right = joystick.get_axis(5)  # RT (Oikea liipaisin)

        if trigger_left > 0.1:  # Jos LT liipaisin painettu
            run_motor(motor6, -int(trigger_left * 1000))  # Moottori 2 taaksepäin
            print(f"Motor 2 running backward at speed: {-int(trigger_left * 1000)}")
        elif trigger_right > 0.1:  # Jos RT liipaisin painettu
            run_motor(motor6, int(trigger_right * 1000))  # Moottori 2 eteenpäin
            print(f"Motor 2 running forward at speed: {int(trigger_right * 1000)}")
        else:
            stop_motor(motor6)  # Pysäytä moottori 2, jos triggereitä ei paineta

except KeyboardInterrupt:
    # Pysäytä kaikki moottorit ja sammuta ohjelma
    stop_motor(motor1)
    stop_motor(motor2)
    stop_motor(motor3)
    stop_motor(motor4)
    stop_motor(motor5)
    stop_motor(motor6)
    stop_motor(motor7)
    print("All motors stopped and program terminated.")
