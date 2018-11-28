from random import randint
import time
'''
def roll_number():
    print('Rolling...')
    time.sleep(0.5)
    print(number)
    
roll_number()
'''
#def setup():
#    global number
number = randint(1,4)

def draw():
    global number
    background(180,180,180)
    fill(0,0,0)
    textSize(20)
    text('Rolling...',7,55)
    fill(255,255,255)
    background(180,180,180)
    rect(25,25,50,50)
    if mousePressed and 25 < mouseX < 75 and 25 < mouseY < 75:
        if number == 1:
            rect(25,25,50,50)
            fill(0,0,0)
            ellipse(50,50,10,10)
        elif number == 2:
            rect(25,25,50,50)
            fill(0,0,0)
            ellipse(35,35,10,10)
            ellipse(65,65,10,10)
        elif number == 3:
            rect(25,25,50,50)
            fill(0,0,0)
            ellipse(50,50,10,10)
            ellipse(35,35,10,10)
            ellipse(65,65,10,10)
        elif number == 4:
            rect(25,25,50,50)
            fill(0,0,0)
            ellipse(35,35,10,10)
            ellipse(35,65,10,10)
            ellipse(65,35,10,10)
            ellipse(65,65,10,10)
