#astronauts
astronaut0 = [1, 1, 3]
astronaut1 = [3, 1, 1]
astronaut2 = [0, 1, 4]

#team
team = [astronaut0,astronaut1,astronaut2]

for axisY in range(3):
    print("Astronaut",axisY)
    for axisX in range (3):
        item = team[axisY][axisX]
        if (axisX == 0) & ( item < 3):
            print("no enough helmets")
        if axisX == 1:
            print("space suits")
        if axisX == 2:
            print("oxygen")
        
