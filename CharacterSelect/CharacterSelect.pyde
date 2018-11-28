def printText():
    fill(0,0,0)
    textSize(32)
    text("Warrior",100,330)
    text("Wizard",353,330)
    text("Rogue",606,330)
    text("Ranger",859,330)
    text("Paladin",100,650)
    text("Monk",358,650)
    text("Warlock",606,650)
    text("Saint",864,650)
    text("Confirm",1185,620)

def setup():
    size(1500, 800)
    fill(255)
    rect(40,40,233,300)
    rect(293,40,233,300)
    rect(546,40,233,300)
    rect(799,40,233,300)
    rect(40,360,233,300)
    rect(293,360,233,300)
    rect(546,360,233,300)
    rect(799,360,233,300)
    fill(150)
    rect(1150,560,200,100)
    printText()

players = 0
war = False
wiz = False
rog = False
ran = False
pal = False
mon = False
warl = False
sai = False

#a function that returns true after something is clicked
def onClick():
    if mousePressed:
        held = True
    if held==True:
        if mousePressed == False:
            return True
    return False
    

    
def mousePressed():
    global players
    global war
    global wiz
    global rog
    global ran
    global pal
    global mon
    global warl
    global sai
    if mousePressed and mouseX > 40 and mouseY > 40 and mouseX < 270 and mouseY < 340 and war == False:
        fill(150)
        players +=1
        war = True
    elif war == True:
        fill(150)
    else:
        fill(255)
    rect(40,40,233,300)
    if mousePressed and mouseX > 293 and mouseY > 40 and mouseX < 526 and mouseY < 340 and wiz == False:
        fill(150)
        players +=1
        wiz = True
    elif wiz == True:
        fill(150)
    else:
        fill(255)
    rect(293,40,233,300)
    if mousePressed and mouseX > 546 and mouseY > 40 and mouseX < 779 and mouseY < 340 and rog == False:
        fill(150)
        players +=1
        rog = True
    elif rog == True:
        fill(150)
    else:
        fill(255)
    rect(546,40,233,300)
    if mousePressed and mouseX > 799 and mouseY > 40 and mouseX < 1032 and mouseY < 340 and ran == False:
        fill(150)
        players +=1
        ran = True
    elif ran == True:
        fill(150)
    else:
        fill(255)
    rect(799,40,233,300)
    if mousePressed and mouseX > 40 and mouseY > 360 and mouseX < 270 and mouseY < 660 and pal == False:
        fill(150)
        players +=1
        pal = True
    elif pal == True:
        fill(150)
    else:
        fill(255)
    rect(40,360,233,300)
    if mousePressed and mouseX > 293 and mouseY > 360 and mouseX < 526 and mouseY < 660 and mon == False:
        fill(150)
        players +=1
        mon = True
    elif mon == True:
        fill(150)
    else:
        fill(255)
    rect(293,360,233,300)
    if mousePressed and mouseX > 546 and mouseY > 360 and mouseX < 779 and mouseY < 660 and warl == False:
        fill(150)
        players +=1
        warl = True
    elif warl == True:
        fill(150)
    else:
        fill(255)
    rect(546,360,233,300)
    if mousePressed and mouseX > 799 and mouseY > 360 and mouseX < 1032 and mouseY < 660 and sai == False:
        fill(150)
        players +=1
        sai = True
    elif sai == True:
        fill(150)
    else:
        fill(255)
    rect(799,360,233,300)
    if players < 2:
        fill(150)
    elif mousePressed and mouseX > 1150 and mouseY > 560 and mouseX < 1350 and mouseY < 660 and players >= 2:
        fill(230)
    else:
        fill(255)
    rect(1150,560,200,100)
    printText()

def draw():
    global players
    
    print(players)
    
    
    
