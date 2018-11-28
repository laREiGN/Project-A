from random import randint
import time

number = 0

def setup():
    fill(255,255,255,255)
    rect(25,25,50,50)
    
def draw_num_1():
    fill(255,255,255,255)
    rect(25,25,50,50)
    fill(0,0,0)
    ellipse(50,50,10,10)

def draw_num_2():
    fill(255,255,255,255)
    rect(25,25,50,50)
    fill(0,0,0)
    ellipse(35,35,10,10)
    ellipse(65,65,10,10)
    
def draw_num_3():
    fill(255,255,255,255)
    rect(25,25,50,50)
    fill(0,0,0)
    ellipse(50,50,10,10)
    ellipse(35,35,10,10)
    ellipse(65,65,10,10)
    
def draw_num_4():
    fill(255,255,255,255)
    rect(25,25,50,50)
    fill(0,0,0)
    ellipse(35,35,10,10)
    ellipse(35,65,10,10)
    ellipse(65,35,10,10)
    ellipse(65,65,10,10)
    
def mousePressed():
    global number

    if 25 < mouseX < 75 and 25 < mouseY < 75:
        number = randint(1,4)
 
def draw():
    global number    

    if number == 1:
        draw_num_1()
    elif number == 2:
        draw_num_2()
    elif number == 3:
        draw_num_3()
    elif number == 4:
        draw_num_4()
        
