turn_count = 1
global_turn_count = 1
players = 4 
currentphase = 1

def setup():
    size(800, 600)
    background(139,0,0)
    
def draw():
    global turn_count
    background(139,0,0)
    fill(255,255,255)
    rect(25,50,250,50)
    fill(0,0,0)
    textSize(15)
    text('Press to add a turn',80,80)
    textSize(20)
    text('Turn count = ',25,150)
    text('Global turn count = ',25,200)
    text('The World Eater is currently on:',25, 250)
    text(turn_count,160,150)
    text(global_turn_count,220,200)
    textSize(30)
    text('Phase: ', 100, 320)
    text(currentphase, 200,320)
    worldeaterphase()
    drawCard()
    
def worldeaterphase():
    global global_turn_count
    global currentphase
    if 0 <= global_turn_count <= 10:
        currentphase = 1
    elif 11 <= global_turn_count <= 30:
        currentphase = 2
    elif 31 <= global_turn_count <= 50:
        currentphase = 3
    else:
        currentphase = 4
    
def mousePressed():
    global turn_count
    global global_turn_count
    global players

    if 25 < mouseX < 275 and 50 < mouseY < 100:
        turn_count += 1
        if turn_count % players == 0:
            global_turn_count += 1
            
def keyPressed():
    global turn_count
    global global_turn_count
    global players
    turn_count += 1
    if turn_count % players == 0:
        global_turn_count += 1
    
            
            
def drawCard():
    if mousePressed:
        if 90 < mouseX < 225 and 290 < mouseY < 325:
            if currentphase == 1:
                phase1 = loadImage("worldeater_phase1.png")
                image(phase1, 400, 100, 300, 420)
            elif currentphase == 2:
                phase2 = loadImage("worldeater_phase2.png")
                image(phase2, 400, 100, 300, 420)
            elif currentphase == 3:
                phase3 = loadImage("worldeater_phase3.png")
                image(phase3, 400, 100, 300, 420)
            elif currentphase == 4:
                phase4 = loadImage("worldeater_phase4.png")
                image(phase4, 400, 100, 300, 420)
                
