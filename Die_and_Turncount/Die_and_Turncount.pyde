from random import randint

number = 2
turn_count = 0
global_turn_count = 0
players = 4

# players moet dan gelinkt worden aan de character selectie om door aan deze variabele de juiste waarde te geven

def setup():
    size(300,250)

def draw_num_1():
    fill(255,255,255,255)
    rect(175,25,50,50)
    fill(0,0,0)
    ellipse(200,50,10,10)

def draw_num_2():
    fill(255,255,255,255)
    rect(175,25,50,50)
    fill(0,0,0)
    ellipse(185,35,10,10)
    ellipse(215,65,10,10)
    
def draw_num_3():
    fill(255,255,255,255)
    rect(175,25,50,50)
    fill(0,0,0)
    ellipse(200,50,10,10)
    ellipse(185,35,10,10)
    ellipse(215,65,10,10)
    
def draw_num_4():
    fill(255,255,255,255)
    rect(175,25,50,50)
    fill(0,0,0)
    ellipse(185,35,10,10)
    ellipse(185,65,10,10)
    ellipse(215,35,10,10)
    ellipse(215,65,10,10)
    
def mousePressed():
    global number
    global turn_count
    global global_turn_count
    global players

    if 25 < mouseX < 125 and 25 < mouseY < 75:
        turn_count += 1
        if turn_count % players == 0:
            global_turn_count += 1
    elif 175 < mouseX < 225 and 25 < mouseY < 75:
        number = randint(1,4)
        
def draw():
    global number
    global turn_count
    background(150,150,150) 
    fill(255,255,255,255)
    rect(25,25,100,50) 
    rect(175,25,50,50)
    fill(0,0,0)
    textSize(10)
    text('Press to add a turn',30,50)
    textSize(20)
    text('Turn count = ',25,100)
    text('Global turn count = ',25,150)
    text(turn_count,160,100)
    text(global_turn_count,220,150)   
    
    if number == 1:
        draw_num_1()
    elif number == 2:
        draw_num_2()
    elif number == 3:
        draw_num_3()
    elif number == 4:
        draw_num_4()
        
