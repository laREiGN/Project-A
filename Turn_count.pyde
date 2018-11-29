turn_count = 0
global_turn_count = 0
players = 4

# players moet dan gelinkt worden aan de character selectie om aan deze variabele de juiste waarde te geven

def setup():
    size(250,250)

def mousePressed():
    global turn_count
    global global_turn_count
    global players

    if 25 < mouseX < 125 and 25 < mouseY < 75:
        turn_count += 1
        if turn_count % players == 0:
            global_turn_count += 1

def draw():
    global turn_count
    background(150,150,150) 
    fill(255,255,255,255)
    rect(25,25,100,50)
    fill(0,0,0)
    textSize(10)
    text('Press to add a turn',30,50)
    textSize(20)
    text('Turn count = ',25,100)
    text('Global turn count = ',25,150)
    text(turn_count,160,100)
    text(global_turn_count,220,150)
