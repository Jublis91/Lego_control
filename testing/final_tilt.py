from pybricks.hubs import TechnicHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = TechnicHub()

motor_root_beam = Motor(Port.C)

# 1600 seems to be the max ??
motor_root_beam.run(1000) # Run the motor left at 1600 degrees/s speed. Forward
print(f"Motor A is running{motor_root_beam.speed()}")
wait(2000)
motor_root_beam.run(-1000)
print(f"Motor A is running{motor_root_beam.speed()}")

wait(2000)

motor_root_beam.stop() # Stop the motor left.
print(f"Motor A is stopped{motor_root_beam.speed()}")

# Mesuring curret to determine when to stop the motor
from pybricks.hubs import TechnicHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Port
from pybricks.tools import wait

hub = TechnicHub()

motor_root_beam = Motor(Port.C)

# Ajetaan moottoria eteenpäin nopeudella 600 astetta sekunnissa
motor_root_beam.run(1600)

# Alustetaan kulmat ja muut muuttujat
last_angle = motor_root_beam.angle()
no_move_threshold = 2  # Pyörimisnopeuden raja, jolla määritetään ettei liiku (esim. 2 astetta sekunnissa)
stall_time = 2  # Aika, jonka moottori voi "lyödä tyhjää" ennen kuin pysäytetään
time_no_move = 0  # Aika, jolloin moottori ei ole liikkunut
angle_change_threshold = 0.5  # Minimimuutos kulmassa, jonka täytyy tapahtua, jotta liike lasketaan

# Muuttuja ajastusta varten
time_waited = 0  # Aika, joka on kulunut moottorin käynnistämisestä

while True:
    current_angle = motor_root_beam.angle()
    current_speed = motor_root_beam.speed()  # Käytetään nopeutta
    current_voltage = hub.battery.voltage()  # Tämä palauttaa jännitteen, ei suoraan virtaa

    # Odotetaan 0.5 sekuntia ennen virrankulutuksen mittaamista
    if time_waited >= 500:  # 0.5 sekuntia = 500 ms
        current_battery_current = hub.battery.current()  # Mittaa akun virran kulutusta (mA)
        print(f"Moottorin kulma: {current_angle}, nopeus: {current_speed}, jännite: {current_voltage}, akkuvirta: {current_battery_current} mA")

        # Jos virta ylittää rajan 500 mA, pysäytetään moottori
        if current_battery_current > 450:
            motor_root_beam.stop()  # Odotetaan 0.1 sekuntia
            print(f"Moottori pysäytettiin, koska akkuvirta {current_battery_current} mA ylitti rajan 450 mA")
            break

    # Viivästetään ajan laskemista
    wait(0.1)
    time_waited += 0.1  # Kasvatetaan odotusaikaa 0.1 sekunnilla

