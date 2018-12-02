charList = [('Warrior', 25, 5, 2, 2, 1), ('Warlock', 15, 2, 2, 3, 5), ('Monk', 15, 2, 4, 4, 2), ('Paladin', 20, 4, 1, 2, 4)]

x = 0
currChar = []
bagi = 0
bstr = 0
bdex = 0
bint = 0
    
    
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

points = 2
finalChars = []

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
        currChar = (classname,HP,strength,dex,agi,intl)
    if mousePressed and 800 < mouseX < 875 and 222 < mouseY < 254 and agi != 5 and points > 0:
        agi += 1
        points -=1
        currChar = (classname,HP,strength,dex,agi,intl)
    if mousePressed and 700 < mouseX < 775 and 272 < mouseY < 304 and intl != bint:
        intl -= 1
        points +=1
        currChar = (classname,HP,strength,dex,agi,intl)
    if mousePressed and 800 < mouseX < 875 and 272 < mouseY < 304 and intl != 5 and points > 0:
        intl += 1
        points -=1
        currChar = (classname,HP,strength,dex,agi,intl)
    if mousePressed and 700 < mouseX < 775 and 322 < mouseY < 354 and strength != bstr:
        strength -= 1
        points +=1
        currChar = (classname,HP,strength,dex,agi,intl)
    if mousePressed and 800 < mouseX < 875 and 322 < mouseY < 354 and strength !=5 and points > 0:
        strength += 1
        points -=1
        currChar = (classname,HP,strength,dex,agi,intl)
    if mousePressed and 700 < mouseX < 775 and 372 < mouseY < 404 and dex != bdex:
        dex -= 1
        points +=1
        currChar = (classname,HP,strength,dex,agi,intl)
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
        

def setup():
    size(1500, 800)
    fill(255)
    background(255)
    setBases(x)
    

def draw():
    global x
    drawCharacter(x)
    drawButtons(x)
