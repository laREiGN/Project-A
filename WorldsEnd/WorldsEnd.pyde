state = 0
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
charInList = 0
currChar = []
bagi = 0
bstr = 0
bdex = 0
bint = 0
points = 2
finalChars = []
warriorimg = 0
wizardimg = 0
rogueimg = 0
rangerimg = 0
paladinimg = 0
monkimg = 0
warlockimg = 0
saintimg = 0

'''Loads the images of the characters'''
def loadCharImg():
    global warriorimg
    global wizardimg
    global rogueimg
    global rangerimg
    global paladinimg
    global monkimg
    global warlockimg
    global saintimg
    warriorimg = loadImage("Warrior.png")
    wizardimg = loadImage("Wizard.png")
    rogueimg = loadImage("Rogue.png")
    rangerimg = loadImage("Ranger.png")
    paladinimg = loadImage("Paladin.png")
    monkimg = loadImage("Monk.png")
    warlockimg = loadImage("Warlock.png")
    saintimg = loadImage("Saint.png")


'''Prints all text that appears in this window for the character selecter'''
def printText():
    global warriorimg
    global wizardimg
    global rogueimg
    global rangerimg
    global paladinimg
    global monkimg
    global warlockimg
    global saintimg
    fill(0,0,0)
    textSize(32)
    text("Warrior",100,330)
    image(warriorimg, 50, 50, 213, 250)
    text("Wizard",353,330)
    image(wizardimg, 303, 50, 213, 250)
    text("Rogue",606,330)
    image(rogueimg, 556, 50, 213, 250)
    text("Ranger",859,330)
    image(rangerimg, 809, 50, 213, 250)
    text("Paladin",100,650)
    image(paladinimg, 50, 370, 213, 250)
    text("Monk",358,650)
    image(monkimg, 303, 370, 213, 250)
    text("Warlock",606,650)
    image(warlockimg, 556, 370, 213, 250)
    text("Saint",864,650)
    image(saintimg, 809, 370, 213, 250)
    text("Confirm",1185,620)
    
'''Sets the base stats for the current character in the stat changer'''
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
    
'''Sets up the title screen/main menu'''
def setup():
    background(139,0,0)
    size(1500, 800)
    fill(218,165,32)
    rect(350,250,800,150)
    rect(350,425,800,150)
    rect(350,600,800,150)
    textSize(200)
    text("World's End", 175, 200)
    fill(0)
    textSize(72)
    text("Start Game", 550, 350)
    text("Text Adventure", 475, 525)
    text("Exit Game", 575, 700)


'''Sets up the character selecter'''
def setup2():
    background(139,0,0)
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
    loadCharImg()
    printText()
    
'''Sets up the stat distributor'''
def setup3():
    global charInList
    size(1500, 800)
    fill(255)
    background(139,0,0)
    setBases(charInList)
    
'''Sets up the letter screen'''
def setup50():
    size(1500,800)
    fill(218,165,32)
    rect(1150,560,200,100)
    fill(0)
    textSize(32)
    text("Continue",1180,620)
    letter = loadImage("letter.png")
    image(letter, 200,0,600,800)

'''Draws all non-changing text in the program in the stat distributor'''
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

'''Draws all changing text in the program, using character x. Stat distributor'''
def drawCharacter(x):
    global currChar
    global warriorimg
    global wizardimg
    global rogueimg
    global rangerimg
    global paladinimg
    global monkimg
    global warlockimg
    global saintimg
    background(139,0,0)
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
    if currChar[0] == "Warrior":
        image(warriorimg, 50, 150, 300, 400)
    elif currChar[0] == "Wizard":
        image(wizardimg, 50, 150, 300, 400)
    elif currChar[0] == "Rogue":
        image(rogueimg, 50, 150, 300, 400)
    elif currChar[0] == "Ranger":
        image(rangerimg, 50, 150, 300, 400)
    elif currChar[0] == "Paladin":
        image(paladinimg, 50, 150, 300, 400)
    elif currChar[0] == "Monk":
        image(monkimg, 50, 150, 300, 400)
    elif currChar[0] == "Warlock":
        image(warlockimg, 50, 150, 300, 400)
    else:
        image(saintimg, 50, 150, 300, 400)
    
'''Draws all buttons for the stat distributor'''
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
    if state == 0:  #title screen
        if mousePressed and 350 < mouseX < 1150 and 250 < mouseY < 400:
            fill(230)
            background(139,0,0)
            state = 50
            setup50()
        if mousePressed and 350 < mouseX < 1150 and 425 < mouseY < 575:
            textSize(24)
            text("Coming soon!", 100, 525)
        if mousePressed and 350 < mouseX < 1150 and 600 < mouseY < 750:
            exit()
    if state == 1:  #character selection
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
            background(139,0,0)
            setup3()
        else:
            fill(255)
        rect(1150,560,200,100)
        printText()
    elif state == 2:  #stat distributor
        global currChar
        global points
        global finalChars
        global charInList
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
            if charInList < len(charList) - 1:
                charInList += 1
                setBases(charInList)
                points = 2
            else:
                print(finalChars)
                state += 1
    if state == 50:  #letter screen
        if mousePressed and 1150 < mouseX < 1350 and 560 < mouseY < 660:
            fill(255)
            state = 1
            background(139,0,0)
            setup2()

def draw():
    global state
    if state == 0:
        return 0
    if state == 1:
        global players
    elif state == 2:
        global charInList
        drawCharacter(charInList)
        drawButtons(charInList)
    elif state == 3:
        background(139,0,0)
    elif state == 50:
        return 0
    
    
    
    
