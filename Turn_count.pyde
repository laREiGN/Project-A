# weet niet of het werkt, maar dit had ik bedacht
turn_count = 20
#global_turn_count = 0
#players = 4


def setup():
    fill(255,255,255,255)
    rect(25,25,50,50)
'''
def global_turn_counter():
    global global_turn_count
    
    if turn_count % players == 0:
        global_turn_count += 1


def turn_counter():
    global turn_count
    if 25 < mouseX < 75 and 25 < mouseY < 75:
        turn_count += 1

def mousePressed():
    global turn_count
    turn_counter()
    print(turn_count)
    print(global_turn_count)

def turn_counter():
    global turn_count
    turn_count += 1 
    print(turn_count)   

turn_counter()
'''

def mousePressed():
    global turn_count
    if 25 < mouseX < 75 and 25 < mouseY < 75:
        turn_count += 1
        #turn_counter()

print(turn_count)       


    
