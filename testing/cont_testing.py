import pygame

# Alusta Pygame ja Xbox-ohjain
pygame.init()
pygame.joystick.init()

# Yhdistä ensimmäinen ohjain
joystick = pygame.joystick.Joystick(0)  # 0 = ensimmäinen ohjain
joystick.init()

print(f"Connected to joystick: {joystick.get_name()}")

# Määritellään nappien nimet
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
}

try:
    while True:
        pygame.event.pump()  # Päivitä tapahtumajono

        # Käy läpi kaikki napit ja tarkista niiden tila
        for i in range(joystick.get_numbuttons()):
            button_state = joystick.get_button(i)  # 0 = ei painettu, 1 = painettu
            if button_state:
                print(f"Button {button_names.get(i, 'Unknown')} pressed (Value: {button_state})")

except KeyboardInterrupt:
    print("Program terminated.")
