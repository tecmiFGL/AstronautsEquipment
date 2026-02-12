import time
astronaut0 = [1,6,3]
astronaut1 = [6,1,1]
astronaut2 = [0,4,4]
mission = int(3)
print("Welcome to the captain list suite")
print("Let's check your astronauts' equipment:")
for astronauts in range(mission):
    print("You're revising Astronaut #", (astronauts + 1))
    time.sleep(3.25)
    if astronauts == 0:
        print("Amount of helmets:", (astronaut0[0]))
        if (astronaut0[0]) < 3:
            time.sleep(1)
            print("WARNING: NOT ENOUGH HELMETS")
    if astronauts == 1:
        print("Amount of helmets:", (astronaut1[0]))
        if (astronaut1[0]) < 3:
            time.sleep(1)
            print("WARNING: NOT ENOUGH HELMETS")
    if astronauts == 2:
        print("Amount of helmets:", (astronaut2[0]))
        if (astronaut2[0]) < 3:
            time.sleep(1)
            print("WARNING: NOT ENOUGH HELMETS")
    time.sleep(2.5)
    if astronauts == 0:
        print("Amount of space suits:", (astronaut0[1]))
        if (astronaut0[1]) < 4:
            time.sleep(1)
            print("WARNING: NOT ENOUGH SPACE SUITS")
    if astronauts == 1:
        print("Amount of space suits:", (astronaut1[1]))
        if (astronaut1[1]) < 4:
            time.sleep(1)
            print("WARNING: NOT ENOUGH SPACE SUITS")
    if astronauts == 2:
        print("Amount of space suits:", (astronaut2[1]))
        if (astronaut2[1]) < 4:
            time.sleep(1)
            print("WARNING: NOT ENOUGH SPACE SUITS")
    time.sleep(2.5)
    if astronauts == 0:
        print("Amount of oxygen tanks:", (astronaut0[2]))
        if (astronaut0[2]) < 3:
            time.sleep(1)
            print("CRITICAL WARNING: NOT ENOUGH OXYGEN TANKS")
    if astronauts == 1:
        print("Amount of oxygen tanks:", (astronaut1[2]))
        if (astronaut1[2]) < 3:
            time.sleep(1)
            print("CRITICAL WARNING: NOT ENOUGH OXYGEN TANKS")
    if astronauts == 2:
        print("Amount of oxygen tanks:", (astronaut2[2]))
        if (astronaut2[2]) < 3:
            time.sleep(1)
            print("CRITICAL WARNING: NOT ENOUGH OXYGEN TANKS")
    time.sleep(4)
print("Let's review your team:")
time.sleep(2)
print("Astronaut1 [Helmets, Space Suits, Oxygen Tanks], Astronaut2 [Helmets, Space Suits, Oxygen Tanks], Astronaut3 [Helmets, Space Suits, Oxygen Tanks]")
totalcrew = [astronaut0, astronaut1, astronaut2]
print(totalcrew)