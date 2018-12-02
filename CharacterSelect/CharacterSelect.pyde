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
charList = []

    
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
    if mousePressed and 40 < mouseX < 270 and 40 < mouseY < 340 and war == False:
        fill(150)
        players +=1
        war = True
        charList.append(("Warrior",25,5,2,2,1))
    elif war == True:
        fill(150)
    else:
        fill(255)
    rect(40,40,233,300)
    if mousePressed and 293 < mouseX < 526 and 40 < mouseY < 340 and wiz == False:
        fill(150)
        players +=1
        wiz = True
        charList.append(("Wizard", 10,2,3,3,5))
    elif wiz == True:
        fill(150)
    else:
        fill(255)
    rect(293,40,233,300)
    if mousePressed and 546 < mouseX < 779 and 40 < mouseY < 340 and rog == False:
        fill(150)
        players +=1
        rog = True
        charList.append(("Rogue", 15,2,3,5,2))
    elif rog == True:
        fill(150)
    else:
        fill(255)
    rect(546,40,233,300)
    if mousePressed and 799 < mouseX < 1032 and 40 < mouseY < 340 and ran == False:
        fill(150)
        players +=1
        ran = True
        charList.append(("Ranger", 15,1,5,4,2))
    elif ran == True:
        fill(150)
    else:
        fill(255)
    rect(799,40,233,300)
    if mousePressed and 40 < mouseX < 270 and 360 < mouseY < 660 and pal == False:
        fill(150)
        players +=1
        pal = True
        charList.append(("Paladin", 20,4,1,2,4))
    elif pal == True:
        fill(150)
    else:
        fill(255)
    rect(40,360,233,300)
    if mousePressed and 293 < mouseX < 526 and 360 < mouseY < 660 and mon == False:
        fill(150)
        players +=1
        mon = True
        charList.append(("Monk", 15,2,4,4,2))
    elif mon == True:
        fill(150)
    else:
        fill(255)
    rect(293,360,233,300)
    if mousePressed and 546 < mouseX < 779 and 360 < mouseY < 660 and warl == False:
        fill(150)
        players +=1
        warl = True
        charList.append(("Warlock", 15,2,2,3,5))
    elif warl == True:
        fill(150)
    else:
        fill(255)
    rect(546,360,233,300)
    if mousePressed and 799 < mouseX < 1032 and 360 < mouseY < 660 and sai == False:
        fill(150)
        players +=1
        sai = True
        charList.append(("Saint", 15,1,3,3,5))
    elif sai == True:
        fill(150)
    else:
        fill(255)
    rect(799,360,233,300)
    if players < 2:
        fill(150)
    elif mousePressed and 1150 < mouseX < 1350 and 560 < mouseY < 660 and players >= 2:
        fill(230)
        print("Amount of players: " + str(players))
        print("Characters chosen: " + str(charList))
    else:
        fill(255)
    rect(1150,560,200,100)
    printText()

def draw():
    global players
    
    
    
    
    
