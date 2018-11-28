from random import randint
import time

number = 0

#rolling = False
#rolling_frame = 0
#rolling_max_frame = 50


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

'''    
def draw_Rolling():
    fill(255,255,255,255)
    rect(25,25,50,50)
    #textSize(32)
    #text('Rolling...',25,25)
    put_Text(25,25,"Rolling...")
    
def put_Text(x,y, s):
    textSize(10)
    text(s,x,y)
'''
    
def mousePressed():
    global number
    #global rolling
    #global rolling_max_frame
    #global rolling_frame
    
    if 25 < mouseX < 75 and 25 < mouseY < 75:
        number = randint(1,4)
        print(number)
        #rolling = True
        #rolling_frame = rolling_max_frame

'''
def my_update():
    global rolling
    global rolling_max_frame
    global rolling_frame
    
    if rolling and rolling_frame > 0:
        rolling_frame -= 1
        
    if rolling_frame == 0:
        rolling = False
'''
    
def draw():
    global number    
    #global rolling
    #global rolling_max_frame
    #global rolling_frame
    
    #my_update()
    
    #if rolling:
    #    draw_Rolling()
    #else:
    if number == 1:
        draw_num_1()
    elif number == 2:
        draw_num_2()
    elif number == 3:
        draw_num_3()
    elif number == 4:
        draw_num_4()
        
