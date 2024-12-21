import pygame
from pybricks.hubs import TechnicHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Port


"""tarkasta mikä portti ohjaa mitäkin moottoria ja kommentoi oikeat koodiin"""

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

"""Tästä eteenpäin pitää muokata, koska tämä on vain esimerkki"""
try:
    while True:
        pygame.event.pump()  # Päivitä tapahtumajono

        # 1. Käytä painikkeita (napit) moottorin toimintaan
        if joystick.get_button(0):  # A-nappi
            motor.run1(500)  # Käynnistä moottori nopeudella 500 deg/s
            print("Motor is running forward!")
        elif joystick.get_button(1):  # B-nappi
            motor.run1(-500)  # Käynnistä moottori taaksepäin nopeudella -500 deg/s
            print("Motor is running backward!")
        elif joystick.get_button(2):  # X-nappi
            motor.stop()  # Pysäytä moottori
            print("Motor stopped.")

        # 2. Käytä triggereitä (liipaisimet) nopeuden ohjaukseen
        trigger_left = joystick.get_axis(2)  # LT (Vasen liipaisin)
        trigger_right = joystick.get_axis(5)  # RT (Oikea liipaisin)

        if trigger_left > 0.1:  # Jos LT liipaisin painettu
            motor.run5(-int(trigger_left * 1000))  # Suureneva nopeus taaksepäin
            print(f"Motor running backward at speed: {-int(trigger_left * 1000)}")
        elif trigger_right > 0.1:  # Jos RT liipaisin painettu
            motor.run6(int(trigger_right * 1000))  # Suureneva nopeus eteenpäin
            print(f"Motor running forward at speed: {int(trigger_right * 1000)}")

except KeyboardInterrupt:
    motor.stop()
    print("Motor stopped and program terminated.")