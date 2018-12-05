
'''Prints all text that appears in this window'''
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
    
def setBases(x):
    global currChar
    global bagi
    global bstr
    global bdex
    global bint
    currChar = list(charList[x])
    bagi = charList[x][4]
    bstr = charList[x][2]
    bdex = charList[x][3]
    bint = charList[x][5]

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
    
def setup2():
    size(1500, 800)
    fill(255)
    background(255)
    setBases(x)
    
state = 1
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
x = 0
currChar = []
bagi = 0
bstr = 0
bdex = 0
bint = 0
points = 2
finalChars = []

'''Draws all non-changing text in the program'''
def drawText():
    textSize(32)
    fill(0)
    text("-",728,248)
    text("-",728,298)
    text("-",728,348)
    text("-",728,398)
    text("+",825,248)
    text("+",825,298)
    text("+",825,348)
    text("+",825,398)
    textSize(72)
    text("Confirm", 485, 575)
    textSize(32)
    text("Back", 50, 575)

'''Draws all changing text in the program, using character x'''
def drawCharacter(x):
    global currChar
    background(255)
    fill(0)
    textSize(72)
    text(charList[x][0],50,100)
    textSize(32)
    text("HP: " + str(currChar[1]),400,200)
    text("Agility: " + str(currChar[4]), 400, 250)
    text("Intelligence: " + str(currChar[5]), 400, 300)
    text("Strength: " + str(currChar[2]), 400, 350)
    text("Dexterity: " + str(currChar[3]), 400, 400)
    text("Stat points left to assign: " + str(points), 400, 450)
    
'''Draws all buttons'''
def drawButtons(x):
    if((currChar[4]) != (charList[x][4])):
        fill(255)
        rect(700, 222, 75, 32)
    else:
        fill(180)
        rect(700, 222, 75, 32)
    if((currChar[5]) != (charList[x][5])):
        fill(255)
        rect(700, 272, 75, 32)
    else:
        fill(180)
        rect(700, 272, 75, 32)
    if((currChar[2]) != (charList[x][2])):
        fill(255)
        rect(700, 322, 75, 32)
    else:
        fill(180)
        rect(700, 322, 75, 32)
    if((currChar[3]) != (charList[x][3])):
        fill(255)
        rect(700, 372, 75, 32)
    else:
        fill(180)
        rect(700, 372, 75, 32)
    
    if((currChar[4]) != 5 and points > 0):
        fill(255)
        rect(800, 222, 75, 32)
    else:
        fill(180)
        rect(800, 222, 75, 32)
    if((currChar[5]) != 5 and points > 0):
        fill(255)
        rect(800, 272, 75, 32)
    else:
        fill(180)
        rect(800, 272, 75, 32)
    if((currChar[2]) != 5 and points > 0):
        fill(255)
        rect(800, 322, 75, 32)
    else:
        fill(180)
        rect(800, 322, 75, 32)
    if((currChar[3]) != 5 and points > 0):
        fill(255)
        rect(800, 372, 75, 32)
    else:
        fill(180)
        rect(800, 372, 75, 32)    
    
    if(points == 0):
        fill(255)
        rect(400, 500, 475, 100)
    else:
        fill(180)
        rect(400, 500, 475, 100)
    drawText()
    
def mousePressed():
    global state
    if state == 1:
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
            state +=1
            background(180)
            setup2()
        else:
            fill(255)
        rect(1150,560,200,100)
        printText()
    elif state == 2:
        global currChar
        global points
        global finalChars
        global x
        classname = currChar[0]
        HP = currChar[1]
        strength = currChar[2]
        dex = currChar[3]
        agi = currChar[4]
        intl = currChar[5]
        if mousePressed and 700 < mouseX < 775 and 222 < mouseY < 254 and agi != bagi:
            agi -= 1
            points +=1
        if mousePressed and 800 < mouseX < 875 and 222 < mouseY < 254 and agi != 5 and points > 0:
            agi += 1
            points -=1
        if mousePressed and 700 < mouseX < 775 and 272 < mouseY < 304 and intl != bint:
            intl -= 1
            points +=1
        if mousePressed and 800 < mouseX < 875 and 272 < mouseY < 304 and intl != 5 and points > 0:
            intl += 1
            points -=1
        if mousePressed and 700 < mouseX < 775 and 322 < mouseY < 354 and strength != bstr:
            strength -= 1
            points +=1
        if mousePressed and 800 < mouseX < 875 and 322 < mouseY < 354 and strength !=5 and points > 0:
            strength += 1
            points -=1
        if mousePressed and 700 < mouseX < 775 and 372 < mouseY < 404 and dex != bdex:
            dex -= 1
            points +=1
        if mousePressed and 800 < mouseX < 875 and 372 < mouseY < 404 and dex != 5 and points > 0:
            dex += 1
            points -=1
        currChar = (classname,HP,strength,dex,agi,intl)
        if mousePressed and 400 < mouseX < 875 and 500 < mouseY < 600 and points == 0:
            finalChars.append(currChar)
            if x < len(charList) - 1:
                x += 1
                setBases(x)
                points = 2
            else:
                print(finalChars)

def draw():
    global state
    if state == 1:
        global players
    elif state == 2:
        global x
        drawCharacter(x)
        drawButtons(x)
    
    
    
    
