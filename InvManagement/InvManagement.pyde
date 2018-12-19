#Binds an inventory state to every player
player_one = {'Equipped1': 'Empty', 'Equipped2': 'Empty', 'Equipped3': 'Empty', 'Additional1': 'Empty', 'Additional2': 'Empty', 'Additional3': 'Empty',  'Additional4': 'Empty',  'Additional5': 'Empty'}
player_two = {'Equipped1': 'Empty', 'Equipped2': 'Empty', 'Equipped3': 'Empty', 'Additional1': 'Empty', 'Additional2': 'Empty', 'Additional3': 'Empty',  'Additional4': 'Empty',  'Additional5': 'Empty'}
player_three = {'Equipped1': 'Empty', 'Equipped2': 'Empty', 'Equipped3': 'Empty', 'Additional1': 'Empty', 'Additional2': 'Empty', 'Additional3': 'Empty',  'Additional4': 'Empty',  'Additional5': 'Empty'}
player_four = {'Equipped1': 'Empty', 'Equipped2': 'Empty', 'Equipped3': 'Empty', 'Additional1': 'Empty', 'Additional2': 'Empty', 'Additional3': 'Empty',  'Additional4': 'Empty',  'Additional5': 'Empty'}
player_five = {'Equipped1': 'Empty', 'Equipped2': 'Empty', 'Equipped3': 'Empty', 'Additional1': 'Empty', 'Additional2': 'Empty', 'Additional3': 'Empty',  'Additional4': 'Empty',  'Additional5': 'Empty'}
player_six = {'Equipped1': 'Empty', 'Equipped2': 'Empty', 'Equipped3': 'Empty', 'Additional1': 'Empty', 'Additional2': 'Empty', 'Additional3': 'Empty',  'Additional4': 'Empty',  'Additional5': 'Empty'}
player_seven = {'Equipped1': 'Empty', 'Equipped2': 'Empty', 'Equipped3': 'Empty', 'Additional1': 'Empty', 'Additional2': 'Empty', 'Additional3': 'Empty',  'Additional4': 'Empty',  'Additional5': 'Empty'}
player_eight = {'Equipped1': 'Empty', 'Equipped2': 'Empty', 'Equipped3': 'Empty', 'Additional1': 'Empty', 'Additional2': 'Empty', 'Additional3': 'Empty',  'Additional4': 'Empty',  'Additional5': 'Empty'}
current_state = player_one

#Global values
playersamt = ('player_one', 'player_two', 'player_three', 'player_four', 'player_five', 'player_six', 'player_seven', 'player_eight')
players = 4
currentplayer = 1
playersused = playersamt[0:int(players)]

ItemsFile = open('Items.txt', 'r')
ArmorFile = open('Armor.txt', 'r')
WeaponsFile = open('Weapons.txt', 'r')
Items = ItemsFile.read().split(', ')
Armor = ArmorFile.read().split(', ')
Weapons = WeaponsFile.read().split(', ')
currentChoices = Items
choicePopupActive = False
inventorySlot = 1

def setup():
    size(800, 600) #1500x800
    background(139,0,0)
    
def draw():
    global choicePopupActive
    playerButtons()
    inventoryLayout()
    inventoryButtons()
    playerChoice()
    playerIndication()
    fullReset()
    if choicePopupActive == True:
        choicePopup()
        cardTypeChoice()
        cardChoice()
    
def playerButtons():
    strokeWeight(1)
    fill(200)
    rect(0, 0, 100, 35) #Draws player screen buttons
    rect(100, 0, 100, 35)
    rect(200, 0, 100, 35)
    rect(300, 0, 100, 35)
    rect(400, 0, 100, 35)
    rect(500, 0, 100, 35)
    rect(600, 0, 100, 35)
    rect(700, 0, 100, 35)
    textSize(20)
    fill(139,0,0)
    text('Player 1', 12, 25) #Player screen button text
    text('Player 2', 112, 25)
    text('Player 3', 212, 25)
    text('Player 4', 312, 25)
    text('Player 5', 412, 25)
    text('Player 6', 512, 25)
    text('Player 7', 612, 25)
    text('Player 8', 712, 25)
    
def playerIndication(): #Tells you what players inventory you are seeing
    textSize(30)
    fill(0)
    text('Player ', 10, 80) #Current players inventory
    text(currentplayer, 105, 80)
    text('s Inventory:', 125, 80)
    
def inventoryLayout(): #Draws the main inventory layout
    textSize(20)
    fill(200)
    strokeWeight(1)
    text('Currently equipped in the first slot:',10,120)
    text(current_state['Equipped1'], 50, 150)
    text('Currently equipped in the second slot:',10,200)
    text(current_state['Equipped2'], 50, 230)
    text('Currently equipped in the third slot:',10,280)
    text(current_state['Equipped3'], 50, 310)
    text('Available in the players inventory:',10,360)
    text(current_state['Additional1'], 50, 390)
    text(current_state['Additional2'], 50, 420)
    text(current_state['Additional3'], 50, 450)
    text(current_state['Additional4'], 50, 480)
    text(current_state['Additional5'], 50, 510)
    
def inventoryButtons(): #Draws the buttons that let you add and remove items from the inventory
    strokeWeight(1)
    fill(200)
    rect(20, 132, 20, 20)
    rect(20, 212, 20, 20)
    rect(20, 292, 20, 20)
    rect(20, 372, 20, 20)
    rect(20, 402, 20, 20)
    rect(20, 432, 20, 20)
    rect(20, 462, 20, 20)
    rect(20, 492, 20, 20)
    fill(0)
    strokeWeight(5)
    line(24, 142, 36, 142)
    line(30, 136, 30, 148)
    line(24, 222, 36, 222)
    line(30, 216, 30, 228)
    line(24, 302, 36, 302)
    line(30, 296, 30, 308)
    line(24, 382, 36, 382)
    line(30, 376, 30, 388)
    line(24, 412, 36, 412)
    line(30, 406, 30, 418)
    line(24, 442, 36, 442)
    line(30, 436, 30, 448)
    line(24, 472, 36, 472)
    line(30, 466, 30, 478)
    line(24, 502, 36, 502)
    line(30, 496, 30, 508)
    
def mousePressed(): #Makes the invnetory slot selection buttons and the inventory category buttons fucntional
    global choicePopupActive
    global inventorySlot
    if 0 < mouseX < 40 and 132 < mouseY < 152:
        choicePopupActive = True
        inventorySlot = 1
    elif 0 < mouseX < 40 and 212 < mouseY < 232:
        choicePopupActive = True
        inventorySlot = 2
    elif 0 < mouseX < 40 and 292 < mouseY < 312:
        choicePopupActive = True
        inventorySlot = 3
    elif 0 < mouseX < 40 and 372 < mouseY < 392:
        choicePopupActive = True
        inventorySlot = 4
    elif 0 < mouseX < 40 and 402 < mouseY < 422:
        choicePopupActive = True
        inventorySlot = 5
    elif 0 < mouseX < 40 and 432 < mouseY < 452:
        choicePopupActive = True
        inventorySlot = 6
    elif 0 < mouseX < 40 and 462 < mouseY < 482:
        choicePopupActive = True
        inventorySlot = 7
    elif 0 < mouseX < 40 and 492 < mouseY < 512:
        choicePopupActive = True
        inventorySlot = 8
    elif 450 < mouseX < 550 and 60 < mouseY < 100:
        currentChoices = Items
    elif 560 < mouseX < 660 and 60 < mouseY < 100:
        currentChoices = Weapons
    elif 670 < mouseX < 780 and 60 < mouseY < 100:
        currentChoices = Armor
            
def choicePopup(): #Draws a popup that lets you pick any of the given items to add to your inventory
    global Items
    global Armor
    global Weapons
    global currentChoices
    global choicePopupActive
    fill(200)
    strokeWeight(2)
    rect(450, 60, 330, 520)
    rect(450,60,110,40)
    rect(560,60,110,40)
    rect(670,60,110,40)
    strokeWeight(1)
    line(617, 100, 617, 580)
    line(450, 100, 780, 100)
    line(450, 120, 780, 120)
    line(450, 140, 780, 140)
    line(450, 160, 780, 160)
    line(450, 180, 780, 180)
    line(450, 200, 780, 200)
    line(450, 220, 780, 220)
    line(450, 240, 780, 240)
    line(450, 260, 780, 260)
    line(450, 280, 780, 280)
    line(450, 300, 780, 300)
    line(450, 320, 780, 320)
    line(450, 340, 780, 340)
    line(450, 360, 780, 360)
    line(450, 380, 780, 380)
    line(450, 400, 780, 400)
    line(450, 420, 780, 420)
    line(450, 440, 780, 440)
    line(450, 460, 780, 460)
    line(450, 480, 780, 480)
    line(450, 500, 780, 500)
    line(450, 520, 780, 520)
    line(450, 540, 780, 540)
    line(450, 560, 780, 560)
    fill(0)
    textSize(20)
    text('Items', 476, 87)
    text('Weapons', 570, 87)
    text('Armor', 690, 87)
    if currentChoices == Items:
        textSize(12)
        text(Items[0], 455, 115)
        text(Items[1], 455, 135)
        text(Items[2], 455, 155)
        text(Items[3], 455, 175)
        text(Items[4], 455, 195)
        text(Items[5], 455, 215)
        text(Items[6], 455, 235)
        text(Items[7], 455, 255)
        text(Items[8], 455, 275)
        text(Items[9], 455, 295)
        text(Items[10], 455, 315)
        text(Items[11], 455, 335)
        text(Items[12], 455, 355)
        text(Items[13], 455, 375)
        text(Items[14], 455, 395)
        text(Items[15], 455, 415)
        text(Items[16], 455, 435)
        text(Items[17], 455, 455)
        text(Items[18], 455, 475)
        text(Items[19], 455, 495)
        text(Items[20], 455, 515)
        text(Items[21], 455, 535)
        text(Items[22], 455, 555)
        text(Items[23], 455, 575)
        text(Items[24], 620, 115)
        text(Items[25], 620, 135)
        text(Items[26], 620, 155)
        text(Items[27], 620, 175)
        text(Items[28], 620, 195)
        text(Items[29], 620, 215)
        text(Items[30], 620, 235)
        text(Items[31], 620, 255)
        text(Items[32], 620, 275)
        text(Items[33], 620, 295)
        text(Items[34], 620, 315)
    elif currentChoices == Weapons:
        textSize(12)
        text(Weapons[0], 455, 115)
        text(Weapons[1], 455, 135)
        text(Weapons[2], 455, 155)
        text(Weapons[3], 455, 175)
        text(Weapons[4], 455, 195)
        text(Weapons[5], 455, 215)
        text(Weapons[6], 455, 235)
        text(Weapons[7], 455, 255)
        text(Weapons[8], 455, 275)
        text(Weapons[9], 455, 295)
        text(Weapons[10], 455, 315)
        text(Weapons[11], 455, 335)
        text(Weapons[12], 455, 355)
        text(Weapons[13], 455, 375)
        text(Weapons[14], 455, 395)
        text(Weapons[15], 455, 415)
        text(Weapons[16], 455, 435)
        text(Weapons[17], 455, 455)
        text(Weapons[18], 455, 475)
        text(Weapons[19], 455, 495)
        text(Weapons[20], 455, 515)
        text(Weapons[21], 455, 535)
        text(Weapons[22], 455, 555)
        text(Weapons[23], 455, 575)
        text(Weapons[24], 620, 115)
        text(Weapons[25], 620, 135)
        text(Weapons[26], 620, 155)
        text(Weapons[27], 620, 175)
        text(Weapons[28], 620, 195)
        text(Weapons[29], 620, 215)
        text(Weapons[30], 620, 235)
    elif currentChoices == Armor:
        textSize(12)
        text(Armor[0], 455, 115)
        text(Armor[1], 455, 135)
        text(Armor[2], 455, 155)
        text(Armor[3], 455, 175)
        text(Armor[4], 455, 195)
        text(Armor[5], 455, 215)
        text(Armor[6], 455, 235)
        text(Armor[7], 455, 255)
        text(Armor[8], 455, 275)
        text(Armor[9], 455, 295)
        text(Armor[10], 455, 315)
        text(Armor[11], 455, 335)
        text(Armor[12], 455, 355)
        text(Armor[13], 455, 375)
        text(Armor[14], 455, 395)
        text(Armor[15], 455, 415)
        text(Armor[16], 455, 435)
        text(Armor[17], 455, 455)
        text(Armor[18], 455, 475)
        text(Armor[19], 455, 495)
        text(Armor[20], 455, 515)
        text(Armor[21], 455, 535)
        text(Armor[22], 455, 555)
        text(Armor[23], 455, 575)
    
def cardTypeChoice():
    global currentChoices
    if mousePressed:
        if 450 < mouseX < 550 and 60 < mouseY < 100:
            currentChoices = Items
        if 550 < mouseX < 650 and 60 < mouseY < 100:
            currentChoices = Weapons
        if 650 < mouseX < 750 and 60 < mouseY < 100:
            currentChoices = Armor
            
def cardChoice(): #Makes the card choice popup functional, assigning an item to the right slot when a button has been clicked
    global currentChoices
    global choicePopupActive
    global currentplayer
    global current_state
    global inventorySlot
    global Items
    global Armor
    global Weapons
    if mousePressed:
        if 450 < mouseX < 600 and 100 < mouseY < 120:
            background(139,0,0)
            if currentChoices == Items:
                if inventorySlot == 1:
                    current_state['Equipped1'] = Items[0]
                elif inventorySlot == 2:
                    current_state['Equipped2'] = Items[0]
                elif inventorySlot == 3:
                    current_state['Equipped3'] = Items[0]
                elif inventorySlot == 4:
                    current_state['Additional1'] = Items[0]
                elif inventorySlot == 5:
                    current_state['Additional2'] = Items[0]
                elif inventorySlot == 6:
                    current_state['Additional3'] = Items[0]
                elif inventorySlot == 7:
                    current_state['Additional4'] = Items[0] 
                elif inventorySlot == 8:
                    current_state['Additional5'] = Items[0]
            elif currentChoices == Weapons:
                if inventorySlot == 1:
                    current_state['Equipped1'] = Weapons[0]
                elif inventorySlot == 2:
                    current_state['Equipped2'] = Weapons[0]
                elif inventorySlot == 3:
                    current_state['Equipped3'] = Weapons[0]
                elif inventorySlot == 3:
                    current_state['Additional1'] = Weapons[0]
                elif inventorySlot == 4:
                    current_state['Additional2'] = Weapons[0]
                elif inventorySlot == 5:
                    current_state['Additional3'] = Weapons[0]
                elif inventorySlot == 6:
                    current_state['Additional4'] = Weapons[0] 
                elif inventorySlot == 7:
                    current_state['Additional5'] = Weapons[0]
            elif currentChoices == Armor:
                if inventorySlot == 1:
                    current_state['Equipped1'] = Armor[0]
                elif inventorySlot == 2:
                    current_state['Equipped2'] = Armor[0]
                elif inventorySlot == 3:
                    current_state['Equipped3'] = Armor[0]
                elif inventorySlot == 3:
                    current_state['Additional1'] = Armor[0]
                elif inventorySlot == 4:
                    current_state['Additional2'] = Armor[0]
                elif inventorySlot == 5:
                    current_state['Additional3'] = Armor[0]
                elif inventorySlot == 6:
                    current_state['Additional4'] = Armor[0] 
                elif inventorySlot == 7:
                    current_state['Additional5'] = Armor[0]
        elif 450 < mouseX < 600 and 120 < mouseY < 140:
            background(139,0,0)
            if currentChoices == Items:
                if inventorySlot == 1:
                    current_state['Equipped1'] = Items[1]
                elif inventorySlot == 2:
                    current_state['Equipped2'] = Items[1]
                elif inventorySlot == 3:
                    current_state['Equipped3'] = Items[1]
                elif inventorySlot == 4:
                    current_state['Additional1'] = Items[1]
                elif inventorySlot == 5:
                    current_state['Additional2'] = Items[1]
                elif inventorySlot == 6:
                    current_state['Additional3'] = Items[1]
                elif inventorySlot == 7:
                    current_state['Additional4'] = Items[1] 
                elif inventorySlot == 8:
                    current_state['Additional5'] = Items[1]
            elif currentChoices == Weapons:
                if inventorySlot == 1:
                    current_state['Equipped1'] = Weapons[1]
                elif inventorySlot == 2:
                    current_state['Equipped2'] = Weapons[1]
                elif inventorySlot == 3:
                    current_state['Equipped3'] = Weapons[1]
                elif inventorySlot == 3:
                    current_state['Additional1'] = Weapons[1]
                elif inventorySlot == 4:
                    current_state['Additional2'] = Weapons[1]
                elif inventorySlot == 5:
                    current_state['Additional3'] = Weapons[1]
                elif inventorySlot == 6:
                    current_state['Additional4'] = Weapons[1] 
                elif inventorySlot == 7:
                    current_state['Additional5'] = Weapons[1]
            elif currentChoices == Armor:
                if inventorySlot == 1:
                    current_state['Equipped1'] = Armor[1]
                elif inventorySlot == 2:
                    current_state['Equipped2'] = Armor[1]
                elif inventorySlot == 3:
                    current_state['Equipped3'] = Armor[1]
                elif inventorySlot == 3:
                    current_state['Additional1'] = Armor[1]
                elif inventorySlot == 4:
                    current_state['Additional2'] = Armor[1]
                elif inventorySlot == 5:
                    current_state['Additional3'] = Armor[1]
                elif inventorySlot == 6:
                    current_state['Additional4'] = Armor[1] 
                elif inventorySlot == 7:
                    current_state['Additional5'] = Armor[1]
        elif 450 < mouseX < 600 and 140 < mouseY < 160:
            background(139,0,0)
            if currentChoices == Items:
                if inventorySlot == 1:
                    current_state['Equipped1'] = Items[2]
                elif inventorySlot == 2:
                    current_state['Equipped2'] = Items[2]
                elif inventorySlot == 3:
                    current_state['Equipped3'] = Items[2]
                elif inventorySlot == 4:
                    current_state['Additional1'] = Items[2]
                elif inventorySlot == 5:
                    current_state['Additional2'] = Items[2]
                elif inventorySlot == 6:
                    current_state['Additional3'] = Items[2]
                elif inventorySlot == 7:
                    current_state['Additional4'] = Items[2] 
                elif inventorySlot == 8:
                    current_state['Additional5'] = Items[2]
            elif currentChoices == Weapons:
                if inventorySlot == 1:
                    current_state['Equipped1'] = Weapons[2]
                elif inventorySlot == 2:
                    current_state['Equipped2'] = Weapons[2]
                elif inventorySlot == 3:
                    current_state['Equipped3'] = Weapons[2]
                elif inventorySlot == 3:
                    current_state['Additional1'] = Weapons[2]
                elif inventorySlot == 4:
                    current_state['Additional2'] = Weapons[2]
                elif inventorySlot == 5:
                    current_state['Additional3'] = Weapons[2]
                elif inventorySlot == 6:
                    current_state['Additional4'] = Weapons[2] 
                elif inventorySlot == 7:
                    current_state['Additional5'] = Weapons[2]
            elif currentChoices == Armor:
                if inventorySlot == 1:
                    current_state['Equipped1'] = Armor[2]
                elif inventorySlot == 2:
                    current_state['Equipped2'] = Armor[2]
                elif inventorySlot == 3:
                    current_state['Equipped3'] = Armor[2]
                elif inventorySlot == 3:
                    current_state['Additional1'] = Armor[2]
                elif inventorySlot == 4:
                    current_state['Additional2'] = Armor[2]
                elif inventorySlot == 5:
                    current_state['Additional3'] = Armor[2]
                elif inventorySlot == 6:
                    current_state['Additional4'] = Armor[2] 
                elif inventorySlot == 7:
                    current_state['Additional5'] = Armor[2]
        elif 450 < mouseX < 600 and 160 < mouseY < 180:
            background(139,0,0)
            if currentChoices == Items:
                if inventorySlot == 1:
                    current_state['Equipped1'] = Items[3]
                elif inventorySlot == 2:
                    current_state['Equipped2'] = Items[3]
                elif inventorySlot == 3:
                    current_state['Equipped3'] = Items[3]
                elif inventorySlot == 4:
                    current_state['Additional1'] = Items[3]
                elif inventorySlot == 5:
                    current_state['Additional2'] = Items[3]
                elif inventorySlot == 6:
                    current_state['Additional3'] = Items[3]
                elif inventorySlot == 7:
                    current_state['Additional4'] = Items[3] 
                elif inventorySlot == 8:
                    current_state['Additional5'] = Items[3]
            elif currentChoices == Weapons:
                if inventorySlot == 1:
                    current_state['Equipped1'] = Weapons[3]
                elif inventorySlot == 2:
                    current_state['Equipped2'] = Weapons[3]
                elif inventorySlot == 3:
                    current_state['Equipped3'] = Weapons[3]
                elif inventorySlot == 3:
                    current_state['Additional1'] = Weapons[3]
                elif inventorySlot == 4:
                    current_state['Additional2'] = Weapons[3]
                elif inventorySlot == 5:
                    current_state['Additional3'] = Weapons[3]
                elif inventorySlot == 6:
                    current_state['Additional4'] = Weapons[3] 
                elif inventorySlot == 7:
                    current_state['Additional5'] = Weapons[3]
            elif currentChoices == Armor:
                if inventorySlot == 1:
                    current_state['Equipped1'] = Armor[3]
                elif inventorySlot == 2:
                    current_state['Equipped2'] = Armor[3]
                elif inventorySlot == 3:
                    current_state['Equipped3'] = Armor[3]
                elif inventorySlot == 3:
                    current_state['Additional1'] = Armor[3]
                elif inventorySlot == 4:
                    current_state['Additional2'] = Armor[3]
                elif inventorySlot == 5:
                    current_state['Additional3'] = Armor[3]
                elif inventorySlot == 6:
                    current_state['Additional4'] = Armor[3] 
                elif inventorySlot == 7:
                    current_state['Additional5'] = Armor[3]
        elif 450 < mouseX < 600 and 180 < mouseY < 200:
            background(139,0,0)
            if currentChoices == Items:
                if inventorySlot == 1:
                    current_state['Equipped1'] = Items[4]
                elif inventorySlot == 2:
                    current_state['Equipped2'] = Items[4]
                elif inventorySlot == 3:
                    current_state['Equipped3'] = Items[4]
                elif inventorySlot == 4:
                    current_state['Additional1'] = Items[4]
                elif inventorySlot == 5:
                    current_state['Additional2'] = Items[4]
                elif inventorySlot == 6:
                    current_state['Additional3'] = Items[4]
                elif inventorySlot == 7:
                    current_state['Additional4'] = Items[4] 
                elif inventorySlot == 8:
                    current_state['Additional5'] = Items[4]
            elif currentChoices == Weapons:
                if inventorySlot == 1:
                    current_state['Equipped1'] = Weapons[4]
                elif inventorySlot == 2:
                    current_state['Equipped2'] = Weapons[4]
                elif inventorySlot == 3:
                    current_state['Equipped3'] = Weapons[4]
                elif inventorySlot == 3:
                    current_state['Additional1'] = Weapons[4]
                elif inventorySlot == 4:
                    current_state['Additional2'] = Weapons[4]
                elif inventorySlot == 5:
                    current_state['Additional3'] = Weapons[4]
                elif inventorySlot == 6:
                    current_state['Additional4'] = Weapons[4] 
                elif inventorySlot == 7:
                    current_state['Additional5'] = Weapons[4]
            elif currentChoices == Armor:
                if inventorySlot == 1:
                    current_state['Equipped1'] = Armor[4]
                elif inventorySlot == 2:
                    current_state['Equipped2'] = Armor[4]
                elif inventorySlot == 3:
                    current_state['Equipped3'] = Armor[4]
                elif inventorySlot == 3:
                    current_state['Additional1'] = Armor[4]
                elif inventorySlot == 4:
                    current_state['Additional2'] = Armor[4]
                elif inventorySlot == 5:
                    current_state['Additional3'] = Armor[4]
                elif inventorySlot == 6:
                    current_state['Additional4'] = Armor[4] 
                elif inventorySlot == 7:
                    current_state['Additional5'] = Armor[4]
        elif 450 < mouseX < 600 and 200 < mouseY < 220:
            background(139,0,0)
            if currentChoices == Items:
                if inventorySlot == 1:
                    current_state['Equipped1'] = Items[5]
                elif inventorySlot == 2:
                    current_state['Equipped2'] = Items[5]
                elif inventorySlot == 3:
                    current_state['Equipped3'] = Items[5]
                elif inventorySlot == 4:
                    current_state['Additional1'] = Items[5]
                elif inventorySlot == 5:
                    current_state['Additional2'] = Items[5]
                elif inventorySlot == 6:
                    current_state['Additional3'] = Items[5]
                elif inventorySlot == 7:
                    current_state['Additional4'] = Items[5] 
                elif inventorySlot == 8:
                    current_state['Additional5'] = Items[5]
            elif currentChoices == Weapons:
                if inventorySlot == 1:
                    current_state['Equipped1'] = Weapons[5]
                elif inventorySlot == 2:
                    current_state['Equipped2'] = Weapons[5]
                elif inventorySlot == 3:
                    current_state['Equipped3'] = Weapons[5]
                elif inventorySlot == 3:
                    current_state['Additional1'] = Weapons[5]
                elif inventorySlot == 4:
                    current_state['Additional2'] = Weapons[5]
                elif inventorySlot == 5:
                    current_state['Additional3'] = Weapons[5]
                elif inventorySlot == 6:
                    current_state['Additional4'] = Weapons[5] 
                elif inventorySlot == 7:
                    current_state['Additional5'] = Weapons[5]
            elif currentChoices == Armor:
                if inventorySlot == 1:
                    current_state['Equipped1'] = Armor[5]
                elif inventorySlot == 2:
                    current_state['Equipped2'] = Armor[5]
                elif inventorySlot == 3:
                    current_state['Equipped3'] = Armor[5]
                elif inventorySlot == 3:
                    current_state['Additional1'] = Armor[5]
                elif inventorySlot == 4:
                    current_state['Additional2'] = Armor[5]
                elif inventorySlot == 5:
                    current_state['Additional3'] = Armor[5]
                elif inventorySlot == 6:
                    current_state['Additional4'] = Armor[5] 
                elif inventorySlot == 7:
                    current_state['Additional5'] = Armor[5]
        elif 450 < mouseX < 600 and 220 < mouseY < 240:
            background(139,0,0)
            if currentChoices == Items:
                if inventorySlot == 1:
                    current_state['Equipped1'] = Items[6]
                elif inventorySlot == 2:
                    current_state['Equipped2'] = Items[6]
                elif inventorySlot == 3:
                    current_state['Equipped3'] = Items[6]
                elif inventorySlot == 4:
                    current_state['Additional1'] = Items[6]
                elif inventorySlot == 5:
                    current_state['Additional2'] = Items[6]
                elif inventorySlot == 6:
                    current_state['Additional3'] = Items[6]
                elif inventorySlot == 7:
                    current_state['Additional4'] = Items[6] 
                elif inventorySlot == 8:
                    current_state['Additional5'] = Items[6]
            elif currentChoices == Weapons:
                if inventorySlot == 1:
                    current_state['Equipped1'] = Weapons[6]
                elif inventorySlot == 2:
                    current_state['Equipped2'] = Weapons[6]
                elif inventorySlot == 3:
                    current_state['Equipped3'] = Weapons[6]
                elif inventorySlot == 3:
                    current_state['Additional1'] = Weapons[6]
                elif inventorySlot == 4:
                    current_state['Additional2'] = Weapons[6]
                elif inventorySlot == 5:
                    current_state['Additional3'] = Weapons[6]
                elif inventorySlot == 6:
                    current_state['Additional4'] = Weapons[6] 
                elif inventorySlot == 7:
                    current_state['Additional5'] = Weapons[6]
            elif currentChoices == Armor:
                if inventorySlot == 1:
                    current_state['Equipped1'] = Armor[6]
                elif inventorySlot == 2:
                    current_state['Equipped2'] = Armor[6]
                elif inventorySlot == 3:
                    current_state['Equipped3'] = Armor[6]
                elif inventorySlot == 3:
                    current_state['Additional1'] = Armor[6]
                elif inventorySlot == 4:
                    current_state['Additional2'] = Armor[6]
                elif inventorySlot == 5:
                    current_state['Additional3'] = Armor[6]
                elif inventorySlot == 6:
                    current_state['Additional4'] = Armor[6] 
                elif inventorySlot == 7:
                    current_state['Additional5'] = Armor[6]
        elif 450 < mouseX < 600 and 240 < mouseY < 260:
            background(139,0,0)
            if currentChoices == Items:
                if inventorySlot == 1:
                    current_state['Equipped1'] = Items[7]
                elif inventorySlot == 2:
                    current_state['Equipped2'] = Items[7]
                elif inventorySlot == 3:
                    current_state['Equipped3'] = Items[7]
                elif inventorySlot == 4:
                    current_state['Additional1'] = Items[7]
                elif inventorySlot == 5:
                    current_state['Additional2'] = Items[7]
                elif inventorySlot == 6:
                    current_state['Additional3'] = Items[7]
                elif inventorySlot == 7:
                    current_state['Additional4'] = Items[7] 
                elif inventorySlot == 8:
                    current_state['Additional5'] = Items[7]
            elif currentChoices == Weapons:
                if inventorySlot == 1:
                    current_state['Equipped1'] = Weapons[7]
                elif inventorySlot == 2:
                    current_state['Equipped2'] = Weapons[7]
                elif inventorySlot == 3:
                    current_state['Equipped3'] = Weapons[7]
                elif inventorySlot == 3:
                    current_state['Additional1'] = Weapons[7]
                elif inventorySlot == 4:
                    current_state['Additional2'] = Weapons[7]
                elif inventorySlot == 5:
                    current_state['Additional3'] = Weapons[7]
                elif inventorySlot == 6:
                    current_state['Additional4'] = Weapons[7] 
                elif inventorySlot == 7:
                    current_state['Additional5'] = Weapons[7]
            elif currentChoices == Armor:
                if inventorySlot == 1:
                    current_state['Equipped1'] = Armor[7]
                elif inventorySlot == 2:
                    current_state['Equipped2'] = Armor[7]
                elif inventorySlot == 3:
                    current_state['Equipped3'] = Armor[7]
                elif inventorySlot == 3:
                    current_state['Additional1'] = Armor[7]
                elif inventorySlot == 4:
                    current_state['Additional2'] = Armor[7]
                elif inventorySlot == 5:
                    current_state['Additional3'] = Armor[7]
                elif inventorySlot == 6:
                    current_state['Additional4'] = Armor[7] 
                elif inventorySlot == 7:
                    current_state['Additional5'] = Armor[7]
        elif 450 < mouseX < 600 and 260 < mouseY < 280:
            background(139,0,0)
            if currentChoices == Items:
                if inventorySlot == 1:
                    current_state['Equipped1'] = Items[8]
                elif inventorySlot == 2:
                    current_state['Equipped2'] = Items[8]
                elif inventorySlot == 3:
                    current_state['Equipped3'] = Items[8]
                elif inventorySlot == 4:
                    current_state['Additional1'] = Items[8]
                elif inventorySlot == 5:
                    current_state['Additional2'] = Items[8]
                elif inventorySlot == 6:
                    current_state['Additional3'] = Items[8]
                elif inventorySlot == 7:
                    current_state['Additional4'] = Items[8] 
                elif inventorySlot == 8:
                    current_state['Additional5'] = Items[8]
            elif currentChoices == Weapons:
                if inventorySlot == 1:
                    current_state['Equipped1'] = Weapons[8]
                elif inventorySlot == 2:
                    current_state['Equipped2'] = Weapons[8]
                elif inventorySlot == 3:
                    current_state['Equipped3'] = Weapons[8]
                elif inventorySlot == 3:
                    current_state['Additional1'] = Weapons[8]
                elif inventorySlot == 4:
                    current_state['Additional2'] = Weapons[8]
                elif inventorySlot == 5:
                    current_state['Additional3'] = Weapons[8]
                elif inventorySlot == 6:
                    current_state['Additional4'] = Weapons[8] 
                elif inventorySlot == 7:
                    current_state['Additional5'] = Weapons[8]
            elif currentChoices == Armor:
                if inventorySlot == 1:
                    current_state['Equipped1'] = Armor[8]
                elif inventorySlot == 2:
                    current_state['Equipped2'] = Armor[8]
                elif inventorySlot == 3:
                    current_state['Equipped3'] = Armor[8]
                elif inventorySlot == 3:
                    current_state['Additional1'] = Armor[8]
                elif inventorySlot == 4:
                    current_state['Additional2'] = Armor[8]
                elif inventorySlot == 5:
                    current_state['Additional3'] = Armor[8]
                elif inventorySlot == 6:
                    current_state['Additional4'] = Armor[8] 
                elif inventorySlot == 7:
                    current_state['Additional5'] = Armor[8]
        elif 450 < mouseX < 600 and 280 < mouseY < 300:
            background(139,0,0)
            if currentChoices == Items:
                if inventorySlot == 1:
                    current_state['Equipped1'] = Items[9]
                elif inventorySlot == 2:
                    current_state['Equipped2'] = Items[9]
                elif inventorySlot == 3:
                    current_state['Equipped3'] = Items[9]
                elif inventorySlot == 4:
                    current_state['Additional1'] = Items[9]
                elif inventorySlot == 5:
                    current_state['Additional2'] = Items[9]
                elif inventorySlot == 6:
                    current_state['Additional3'] = Items[9]
                elif inventorySlot == 7:
                    current_state['Additional4'] = Items[9] 
                elif inventorySlot == 8:
                    current_state['Additional5'] = Items[9]
            elif currentChoices == Weapons:
                if inventorySlot == 1:
                    current_state['Equipped1'] = Weapons[9]
                elif inventorySlot == 2:
                    current_state['Equipped2'] = Weapons[9]
                elif inventorySlot == 3:
                    current_state['Equipped3'] = Weapons[9]
                elif inventorySlot == 3:
                    current_state['Additional1'] = Weapons[9]
                elif inventorySlot == 4:
                    current_state['Additional2'] = Weapons[9]
                elif inventorySlot == 5:
                    current_state['Additional3'] = Weapons[9]
                elif inventorySlot == 6:
                    current_state['Additional4'] = Weapons[9] 
                elif inventorySlot == 7:
                    current_state['Additional5'] = Weapons[9]
            elif currentChoices == Armor:
                if inventorySlot == 1:
                    current_state['Equipped1'] = Armor[9]
                elif inventorySlot == 2:
                    current_state['Equipped2'] = Armor[9]
                elif inventorySlot == 3:
                    current_state['Equipped3'] = Armor[9]
                elif inventorySlot == 3:
                    current_state['Additional1'] = Armor[9]
                elif inventorySlot == 4:
                    current_state['Additional2'] = Armor[9]
                elif inventorySlot == 5:
                    current_state['Additional3'] = Armor[9]
                elif inventorySlot == 6:
                    current_state['Additional4'] = Armor[9] 
                elif inventorySlot == 7:
                    current_state['Additional5'] = Armor[9]
        elif 450 < mouseX < 600 and 300 < mouseY < 320:
            background(139,0,0)
            if currentChoices == Items:
                if inventorySlot == 1:
                    current_state['Equipped1'] = Items[10]
                elif inventorySlot == 2:
                    current_state['Equipped2'] = Items[10]
                elif inventorySlot == 3:
                    current_state['Equipped3'] = Items[10]
                elif inventorySlot == 4:
                    current_state['Additional1'] = Items[10]
                elif inventorySlot == 5:
                    current_state['Additional2'] = Items[10]
                elif inventorySlot == 6:
                    current_state['Additional3'] = Items[10]
                elif inventorySlot == 7:
                    current_state['Additional4'] = Items[10] 
                elif inventorySlot == 8:
                    current_state['Additional5'] = Items[10]
            elif currentChoices == Weapons:
                if inventorySlot == 1:
                    current_state['Equipped1'] = Weapons[10]
                elif inventorySlot == 2:
                    current_state['Equipped2'] = Weapons[10]
                elif inventorySlot == 3:
                    current_state['Equipped3'] = Weapons[10]
                elif inventorySlot == 3:
                    current_state['Additional1'] = Weapons[10]
                elif inventorySlot == 4:
                    current_state['Additional2'] = Weapons[10]
                elif inventorySlot == 5:
                    current_state['Additional3'] = Weapons[10]
                elif inventorySlot == 6:
                    current_state['Additional4'] = Weapons[10] 
                elif inventorySlot == 7:
                    current_state['Additional5'] = Weapons[10]
            elif currentChoices == Armor:
                if inventorySlot == 1:
                    current_state['Equipped1'] = Armor[10]
                elif inventorySlot == 2:
                    current_state['Equipped2'] = Armor[10]
                elif inventorySlot == 3:
                    current_state['Equipped3'] = Armor[10]
                elif inventorySlot == 3:
                    current_state['Additional1'] = Armor[10]
                elif inventorySlot == 4:
                    current_state['Additional2'] = Armor[10]
                elif inventorySlot == 5:
                    current_state['Additional3'] = Armor[10]
                elif inventorySlot == 6:
                    current_state['Additional4'] = Armor[10] 
                elif inventorySlot == 7:
                    current_state['Additional5'] = Armor[10]
        elif 450 < mouseX < 600 and 320 < mouseY < 340:
            background(139,0,0)
            if currentChoices == Items:
                if inventorySlot == 1:
                    current_state['Equipped1'] = Items[11]
                elif inventorySlot == 2:
                    current_state['Equipped2'] = Items[11]
                elif inventorySlot == 3:
                    current_state['Equipped3'] = Items[11]
                elif inventorySlot == 4:
                    current_state['Additional1'] = Items[11]
                elif inventorySlot == 5:
                    current_state['Additional2'] = Items[11]
                elif inventorySlot == 6:
                    current_state['Additional3'] = Items[11]
                elif inventorySlot == 7:
                    current_state['Additional4'] = Items[11] 
                elif inventorySlot == 8:
                    current_state['Additional5'] = Items[11]
            elif currentChoices == Weapons:
                if inventorySlot == 1:
                    current_state['Equipped1'] = Weapons[11]
                elif inventorySlot == 2:
                    current_state['Equipped2'] = Weapons[11]
                elif inventorySlot == 3:
                    current_state['Equipped3'] = Weapons[11]
                elif inventorySlot == 3:
                    current_state['Additional1'] = Weapons[11]
                elif inventorySlot == 4:
                    current_state['Additional2'] = Weapons[11]
                elif inventorySlot == 5:
                    current_state['Additional3'] = Weapons[11]
                elif inventorySlot == 6:
                    current_state['Additional4'] = Weapons[11] 
                elif inventorySlot == 7:
                    current_state['Additional5'] = Weapons[11]
            elif currentChoices == Armor:
                if inventorySlot == 1:
                    current_state['Equipped1'] = Armor[11]
                elif inventorySlot == 2:
                    current_state['Equipped2'] = Armor[11]
                elif inventorySlot == 3:
                    current_state['Equipped3'] = Armor[11]
                elif inventorySlot == 3:
                    current_state['Additional1'] = Armor[11]
                elif inventorySlot == 4:
                    current_state['Additional2'] = Armor[11]
                elif inventorySlot == 5:
                    current_state['Additional3'] = Armor[11]
                elif inventorySlot == 6:
                    current_state['Additional4'] = Armor[11] 
                elif inventorySlot == 7:
                    current_state['Additional5'] = Armor[11]
        elif 450 < mouseX < 600 and 340 < mouseY < 360:
            background(139,0,0)
            if currentChoices == Items:
                if inventorySlot == 1:
                    current_state['Equipped1'] = Items[12]
                elif inventorySlot == 2:
                    current_state['Equipped2'] = Items[12]
                elif inventorySlot == 3:
                    current_state['Equipped3'] = Items[12]
                elif inventorySlot == 4:
                    current_state['Additional1'] = Items[12]
                elif inventorySlot == 5:
                    current_state['Additional2'] = Items[12]
                elif inventorySlot == 6:
                    current_state['Additional3'] = Items[12]
                elif inventorySlot == 7:
                    current_state['Additional4'] = Items[12] 
                elif inventorySlot == 8:
                    current_state['Additional5'] = Items[12]
            elif currentChoices == Weapons:
                if inventorySlot == 1:
                    current_state['Equipped1'] = Weapons[12]
                elif inventorySlot == 2:
                    current_state['Equipped2'] = Weapons[12]
                elif inventorySlot == 3:
                    current_state['Equipped3'] = Weapons[12]
                elif inventorySlot == 3:
                    current_state['Additional1'] = Weapons[12]
                elif inventorySlot == 4:
                    current_state['Additional2'] = Weapons[12]
                elif inventorySlot == 5:
                    current_state['Additional3'] = Weapons[12]
                elif inventorySlot == 6:
                    current_state['Additional4'] = Weapons[12] 
                elif inventorySlot == 7:
                    current_state['Additional5'] = Weapons[12]
            elif currentChoices == Armor:
                if inventorySlot == 1:
                    current_state['Equipped1'] = Armor[12]
                elif inventorySlot == 2:
                    current_state['Equipped2'] = Armor[12]
                elif inventorySlot == 3:
                    current_state['Equipped3'] = Armor[12]
                elif inventorySlot == 3:
                    current_state['Additional1'] = Armor[12]
                elif inventorySlot == 4:
                    current_state['Additional2'] = Armor[12]
                elif inventorySlot == 5:
                    current_state['Additional3'] = Armor[12]
                elif inventorySlot == 6:
                    current_state['Additional4'] = Armor[12] 
                elif inventorySlot == 7:
                    current_state['Additional5'] = Armor[12]
        elif 450 < mouseX < 600 and 360 < mouseY < 380:
            background(139,0,0)
            if currentChoices == Items:
                if inventorySlot == 1:
                    current_state['Equipped1'] = Items[13]
                elif inventorySlot == 2:
                    current_state['Equipped2'] = Items[13]
                elif inventorySlot == 3:
                    current_state['Equipped3'] = Items[13]
                elif inventorySlot == 4:
                    current_state['Additional1'] = Items[13]
                elif inventorySlot == 5:
                    current_state['Additional2'] = Items[13]
                elif inventorySlot == 6:
                    current_state['Additional3'] = Items[13]
                elif inventorySlot == 7:
                    current_state['Additional4'] = Items[13] 
                elif inventorySlot == 8:
                    current_state['Additional5'] = Items[13]
            elif currentChoices == Weapons:
                if inventorySlot == 1:
                    current_state['Equipped1'] = Weapons[13]
                elif inventorySlot == 2:
                    current_state['Equipped2'] = Weapons[13]
                elif inventorySlot == 3:
                    current_state['Equipped3'] = Weapons[13]
                elif inventorySlot == 3:
                    current_state['Additional1'] = Weapons[13]
                elif inventorySlot == 4:
                    current_state['Additional2'] = Weapons[13]
                elif inventorySlot == 5:
                    current_state['Additional3'] = Weapons[13]
                elif inventorySlot == 6:
                    current_state['Additional4'] = Weapons[13] 
                elif inventorySlot == 7:
                    current_state['Additional5'] = Weapons[13]
            elif currentChoices == Armor:
                if inventorySlot == 1:
                    current_state['Equipped1'] = Armor[13]
                elif inventorySlot == 2:
                    current_state['Equipped2'] = Armor[13]
                elif inventorySlot == 3:
                    current_state['Equipped3'] = Armor[13]
                elif inventorySlot == 3:
                    current_state['Additional1'] = Armor[13]
                elif inventorySlot == 4:
                    current_state['Additional2'] = Armor[13]
                elif inventorySlot == 5:
                    current_state['Additional3'] = Armor[13]
                elif inventorySlot == 6:
                    current_state['Additional4'] = Armor[13] 
                elif inventorySlot == 7:
                    current_state['Additional5'] = Armor[13]
        elif 450 < mouseX < 600 and 380 < mouseY < 400:
            background(139,0,0)
            if currentChoices == Items:
                if inventorySlot == 1:
                    current_state['Equipped1'] = Items[14]
                elif inventorySlot == 2:
                    current_state['Equipped2'] = Items[14]
                elif inventorySlot == 3:
                    current_state['Equipped3'] = Items[14]
                elif inventorySlot == 4:
                    current_state['Additional1'] = Items[14]
                elif inventorySlot == 5:
                    current_state['Additional2'] = Items[14]
                elif inventorySlot == 6:
                    current_state['Additional3'] = Items[14]
                elif inventorySlot == 7:
                    current_state['Additional4'] = Items[14] 
                elif inventorySlot == 8:
                    current_state['Additional5'] = Items[14]
            elif currentChoices == Weapons:
                if inventorySlot == 1:
                    current_state['Equipped1'] = Weapons[14]
                elif inventorySlot == 2:
                    current_state['Equipped2'] = Weapons[14]
                elif inventorySlot == 3:
                    current_state['Equipped3'] = Weapons[14]
                elif inventorySlot == 3:
                    current_state['Additional1'] = Weapons[14]
                elif inventorySlot == 4:
                    current_state['Additional2'] = Weapons[14]
                elif inventorySlot == 5:
                    current_state['Additional3'] = Weapons[14]
                elif inventorySlot == 6:
                    current_state['Additional4'] = Weapons[14] 
                elif inventorySlot == 7:
                    current_state['Additional5'] = Weapons[14]
            elif currentChoices == Armor:
                if inventorySlot == 1:
                    current_state['Equipped1'] = Armor[14]
                elif inventorySlot == 2:
                    current_state['Equipped2'] = Armor[14]
                elif inventorySlot == 3:
                    current_state['Equipped3'] = Armor[14]
                elif inventorySlot == 3:
                    current_state['Additional1'] = Armor[14]
                elif inventorySlot == 4:
                    current_state['Additional2'] = Armor[14]
                elif inventorySlot == 5:
                    current_state['Additional3'] = Armor[14]
                elif inventorySlot == 6:
                    current_state['Additional4'] = Armor[14] 
                elif inventorySlot == 7:
                    current_state['Additional5'] = Armor[14]
        elif 450 < mouseX < 600 and 400 < mouseY < 420:
            background(139,0,0)
            if currentChoices == Items:
                if inventorySlot == 1:
                    current_state['Equipped1'] = Items[15]
                elif inventorySlot == 2:
                    current_state['Equipped2'] = Items[15]
                elif inventorySlot == 3:
                    current_state['Equipped3'] = Items[15]
                elif inventorySlot == 4:
                    current_state['Additional1'] = Items[15]
                elif inventorySlot == 5:
                    current_state['Additional2'] = Items[15]
                elif inventorySlot == 6:
                    current_state['Additional3'] = Items[15]
                elif inventorySlot == 7:
                    current_state['Additional4'] = Items[15] 
                elif inventorySlot == 8:
                    current_state['Additional5'] = Items[15]
            elif currentChoices == Weapons:
                if inventorySlot == 1:
                    current_state['Equipped1'] = Weapons[15]
                elif inventorySlot == 2:
                    current_state['Equipped2'] = Weapons[15]
                elif inventorySlot == 3:
                    current_state['Equipped3'] = Weapons[15]
                elif inventorySlot == 3:
                    current_state['Additional1'] = Weapons[15]
                elif inventorySlot == 4:
                    current_state['Additional2'] = Weapons[15]
                elif inventorySlot == 5:
                    current_state['Additional3'] = Weapons[15]
                elif inventorySlot == 6:
                    current_state['Additional4'] = Weapons[15] 
                elif inventorySlot == 7:
                    current_state['Additional5'] = Weapons[15]
            elif currentChoices == Armor:
                if inventorySlot == 1:
                    current_state['Equipped1'] = Armor[15]
                elif inventorySlot == 2:
                    current_state['Equipped2'] = Armor[15]
                elif inventorySlot == 3:
                    current_state['Equipped3'] = Armor[15]
                elif inventorySlot == 3:
                    current_state['Additional1'] = Armor[15]
                elif inventorySlot == 4:
                    current_state['Additional2'] = Armor[15]
                elif inventorySlot == 5:
                    current_state['Additional3'] = Armor[15]
                elif inventorySlot == 6:
                    current_state['Additional4'] = Armor[15] 
                elif inventorySlot == 7:
                    current_state['Additional5'] = Armor[15]
        elif 450 < mouseX < 600 and 420 < mouseY < 440:
            background(139,0,0)
            if currentChoices == Items:
                if inventorySlot == 1:
                    current_state['Equipped1'] = Items[16]
                elif inventorySlot == 2:
                    current_state['Equipped2'] = Items[16]
                elif inventorySlot == 3:
                    current_state['Equipped3'] = Items[16]
                elif inventorySlot == 4:
                    current_state['Additional1'] = Items[16]
                elif inventorySlot == 5:
                    current_state['Additional2'] = Items[16]
                elif inventorySlot == 6:
                    current_state['Additional3'] = Items[16]
                elif inventorySlot == 7:
                    current_state['Additional4'] = Items[16] 
                elif inventorySlot == 8:
                    current_state['Additional5'] = Items[16]
            elif currentChoices == Weapons:
                if inventorySlot == 1:
                    current_state['Equipped1'] = Weapons[16]
                elif inventorySlot == 2:
                    current_state['Equipped2'] = Weapons[16]
                elif inventorySlot == 3:
                    current_state['Equipped3'] = Weapons[16]
                elif inventorySlot == 3:
                    current_state['Additional1'] = Weapons[16]
                elif inventorySlot == 4:
                    current_state['Additional2'] = Weapons[16]
                elif inventorySlot == 5:
                    current_state['Additional3'] = Weapons[16]
                elif inventorySlot == 6:
                    current_state['Additional4'] = Weapons[16] 
                elif inventorySlot == 7:
                    current_state['Additional5'] = Weapons[16]
            elif currentChoices == Armor:
                if inventorySlot == 1:
                    current_state['Equipped1'] = Armor[16]
                elif inventorySlot == 2:
                    current_state['Equipped2'] = Armor[16]
                elif inventorySlot == 3:
                    current_state['Equipped3'] = Armor[16]
                elif inventorySlot == 3:
                    current_state['Additional1'] = Armor[16]
                elif inventorySlot == 4:
                    current_state['Additional2'] = Armor[16]
                elif inventorySlot == 5:
                    current_state['Additional3'] = Armor[16]
                elif inventorySlot == 6:
                    current_state['Additional4'] = Armor[16] 
                elif inventorySlot == 7:
                    current_state['Additional5'] = Armor[16]
        elif 450 < mouseX < 600 and 440 < mouseY < 460:
            background(139,0,0)
            if currentChoices == Items:
                if inventorySlot == 1:
                    current_state['Equipped1'] = Items[17]
                elif inventorySlot == 2:
                    current_state['Equipped2'] = Items[17]
                elif inventorySlot == 3:
                    current_state['Equipped3'] = Items[17]
                elif inventorySlot == 4:
                    current_state['Additional1'] = Items[17]
                elif inventorySlot == 5:
                    current_state['Additional2'] = Items[17]
                elif inventorySlot == 6:
                    current_state['Additional3'] = Items[17]
                elif inventorySlot == 7:
                    current_state['Additional4'] = Items[17] 
                elif inventorySlot == 8:
                    current_state['Additional5'] = Items[17]
            elif currentChoices == Weapons:
                if inventorySlot == 1:
                    current_state['Equipped1'] = Weapons[17]
                elif inventorySlot == 2:
                    current_state['Equipped2'] = Weapons[17]
                elif inventorySlot == 3:
                    current_state['Equipped3'] = Weapons[17]
                elif inventorySlot == 3:
                    current_state['Additional1'] = Weapons[17]
                elif inventorySlot == 4:
                    current_state['Additional2'] = Weapons[17]
                elif inventorySlot == 5:
                    current_state['Additional3'] = Weapons[17]
                elif inventorySlot == 6:
                    current_state['Additional4'] = Weapons[17] 
                elif inventorySlot == 7:
                    current_state['Additional5'] = Weapons[17]
            elif currentChoices == Armor:
                if inventorySlot == 1:
                    current_state['Equipped1'] = Armor[17]
                elif inventorySlot == 2:
                    current_state['Equipped2'] = Armor[17]
                elif inventorySlot == 3:
                    current_state['Equipped3'] = Armor[17]
                elif inventorySlot == 3:
                    current_state['Additional1'] = Armor[17]
                elif inventorySlot == 4:
                    current_state['Additional2'] = Armor[17]
                elif inventorySlot == 5:
                    current_state['Additional3'] = Armor[17]
                elif inventorySlot == 6:
                    current_state['Additional4'] = Armor[17] 
                elif inventorySlot == 7:
                    current_state['Additional5'] = Armor[17]
        elif 450 < mouseX < 600 and 460 < mouseY < 480:
            background(139,0,0)
            if currentChoices == Items:
                if inventorySlot == 1:
                    current_state['Equipped1'] = Items[18]
                elif inventorySlot == 2:
                    current_state['Equipped2'] = Items[18]
                elif inventorySlot == 3:
                    current_state['Equipped3'] = Items[18]
                elif inventorySlot == 4:
                    current_state['Additional1'] = Items[18]
                elif inventorySlot == 5:
                    current_state['Additional2'] = Items[18]
                elif inventorySlot == 6:
                    current_state['Additional3'] = Items[18]
                elif inventorySlot == 7:
                    current_state['Additional4'] = Items[18] 
                elif inventorySlot == 8:
                    current_state['Additional5'] = Items[18]
            elif currentChoices == Weapons:
                if inventorySlot == 1:
                    current_state['Equipped1'] = Weapons[18]
                elif inventorySlot == 2:
                    current_state['Equipped2'] = Weapons[18]
                elif inventorySlot == 3:
                    current_state['Equipped3'] = Weapons[18]
                elif inventorySlot == 3:
                    current_state['Additional1'] = Weapons[18]
                elif inventorySlot == 4:
                    current_state['Additional2'] = Weapons[18]
                elif inventorySlot == 5:
                    current_state['Additional3'] = Weapons[18]
                elif inventorySlot == 6:
                    current_state['Additional4'] = Weapons[18] 
                elif inventorySlot == 7:
                    current_state['Additional5'] = Weapons[18]
            elif currentChoices == Armor:
                if inventorySlot == 1:
                    current_state['Equipped1'] = Armor[18]
                elif inventorySlot == 2:
                    current_state['Equipped2'] = Armor[18]
                elif inventorySlot == 3:
                    current_state['Equipped3'] = Armor[18]
                elif inventorySlot == 3:
                    current_state['Additional1'] = Armor[18]
                elif inventorySlot == 4:
                    current_state['Additional2'] = Armor[18]
                elif inventorySlot == 5:
                    current_state['Additional3'] = Armor[18]
                elif inventorySlot == 6:
                    current_state['Additional4'] = Armor[18] 
                elif inventorySlot == 7:
                    current_state['Additional5'] = Armor[18]
        elif 450 < mouseX < 600 and 480 < mouseY < 500:
            background(139,0,0)
            if currentChoices == Items:
                if inventorySlot == 1:
                    current_state['Equipped1'] = Items[19]
                elif inventorySlot == 2:
                    current_state['Equipped2'] = Items[19]
                elif inventorySlot == 3:
                    current_state['Equipped3'] = Items[19]
                elif inventorySlot == 4:
                    current_state['Additional1'] = Items[19]
                elif inventorySlot == 5:
                    current_state['Additional2'] = Items[19]
                elif inventorySlot == 6:
                    current_state['Additional3'] = Items[19]
                elif inventorySlot == 7:
                    current_state['Additional4'] = Items[19] 
                elif inventorySlot == 8:
                    current_state['Additional5'] = Items[19]
            elif currentChoices == Weapons:
                if inventorySlot == 1:
                    current_state['Equipped1'] = Weapons[19]
                elif inventorySlot == 2:
                    current_state['Equipped2'] = Weapons[19]
                elif inventorySlot == 3:
                    current_state['Equipped3'] = Weapons[19]
                elif inventorySlot == 3:
                    current_state['Additional1'] = Weapons[19]
                elif inventorySlot == 4:
                    current_state['Additional2'] = Weapons[19]
                elif inventorySlot == 5:
                    current_state['Additional3'] = Weapons[19]
                elif inventorySlot == 6:
                    current_state['Additional4'] = Weapons[19] 
                elif inventorySlot == 7:
                    current_state['Additional5'] = Weapons[19]
            elif currentChoices == Armor:
                if inventorySlot == 1:
                    current_state['Equipped1'] = Armor[19]
                elif inventorySlot == 2:
                    current_state['Equipped2'] = Armor[19]
                elif inventorySlot == 3:
                    current_state['Equipped3'] = Armor[19]
                elif inventorySlot == 3:
                    current_state['Additional1'] = Armor[19]
                elif inventorySlot == 4:
                    current_state['Additional2'] = Armor[19]
                elif inventorySlot == 5:
                    current_state['Additional3'] = Armor[19]
                elif inventorySlot == 6:
                    current_state['Additional4'] = Armor[19] 
                elif inventorySlot == 7:
                    current_state['Additional5'] = Armor[19]
        elif 450 < mouseX < 600 and 500 < mouseY < 520:
            background(139,0,0)
            if currentChoices == Items:
                if inventorySlot == 1:
                    current_state['Equipped1'] = Items[20]
                elif inventorySlot == 2:
                    current_state['Equipped2'] = Items[20]
                elif inventorySlot == 3:
                    current_state['Equipped3'] = Items[20]
                elif inventorySlot == 4:
                    current_state['Additional1'] = Items[20]
                elif inventorySlot == 5:
                    current_state['Additional2'] = Items[20]
                elif inventorySlot == 6:
                    current_state['Additional3'] = Items[20]
                elif inventorySlot == 7:
                    current_state['Additional4'] = Items[20] 
                elif inventorySlot == 8:
                    current_state['Additional5'] = Items[20]
            elif currentChoices == Weapons:
                if inventorySlot == 1:
                    current_state['Equipped1'] = Weapons[20]
                elif inventorySlot == 2:
                    current_state['Equipped2'] = Weapons[20]
                elif inventorySlot == 3:
                    current_state['Equipped3'] = Weapons[20]
                elif inventorySlot == 3:
                    current_state['Additional1'] = Weapons[20]
                elif inventorySlot == 4:
                    current_state['Additional2'] = Weapons[20]
                elif inventorySlot == 5:
                    current_state['Additional3'] = Weapons[20]
                elif inventorySlot == 6:
                    current_state['Additional4'] = Weapons[20] 
                elif inventorySlot == 7:
                    current_state['Additional5'] = Weapons[20]
            elif currentChoices == Armor:
                if inventorySlot == 1:
                    current_state['Equipped1'] = Armor[20]
                elif inventorySlot == 2:
                    current_state['Equipped2'] = Armor[20]
                elif inventorySlot == 3:
                    current_state['Equipped3'] = Armor[20]
                elif inventorySlot == 3:
                    current_state['Additional1'] = Armor[20]
                elif inventorySlot == 4:
                    current_state['Additional2'] = Armor[20]
                elif inventorySlot == 5:
                    current_state['Additional3'] = Armor[20]
                elif inventorySlot == 6:
                    current_state['Additional4'] = Armor[20] 
                elif inventorySlot == 7:
                    current_state['Additional5'] = Armor[20]
        elif 450 < mouseX < 600 and 520 < mouseY < 540:
            background(139,0,0)
            if currentChoices == Items:
                if inventorySlot == 1:
                    current_state['Equipped1'] = Items[21]
                elif inventorySlot == 2:
                    current_state['Equipped2'] = Items[21]
                elif inventorySlot == 3:
                    current_state['Equipped3'] = Items[21]
                elif inventorySlot == 4:
                    current_state['Additional1'] = Items[21]
                elif inventorySlot == 5:
                    current_state['Additional2'] = Items[21]
                elif inventorySlot == 6:
                    current_state['Additional3'] = Items[21]
                elif inventorySlot == 7:
                    current_state['Additional4'] = Items[21] 
                elif inventorySlot == 8:
                    current_state['Additional5'] = Items[21]
            elif currentChoices == Weapons:
                if inventorySlot == 1:
                    current_state['Equipped1'] = Weapons[21]
                elif inventorySlot == 2:
                    current_state['Equipped2'] = Weapons[21]
                elif inventorySlot == 3:
                    current_state['Equipped3'] = Weapons[21]
                elif inventorySlot == 3:
                    current_state['Additional1'] = Weapons[21]
                elif inventorySlot == 4:
                    current_state['Additional2'] = Weapons[21]
                elif inventorySlot == 5:
                    current_state['Additional3'] = Weapons[21]
                elif inventorySlot == 6:
                    current_state['Additional4'] = Weapons[21] 
                elif inventorySlot == 7:
                    current_state['Additional5'] = Weapons[21]
            elif currentChoices == Armor:
                if inventorySlot == 1:
                    current_state['Equipped1'] = Armor[21]
                elif inventorySlot == 2:
                    current_state['Equipped2'] = Armor[21]
                elif inventorySlot == 3:
                    current_state['Equipped3'] = Armor[21]
                elif inventorySlot == 3:
                    current_state['Additional1'] = Armor[21]
                elif inventorySlot == 4:
                    current_state['Additional2'] = Armor[21]
                elif inventorySlot == 5:
                    current_state['Additional3'] = Armor[21]
                elif inventorySlot == 6:
                    current_state['Additional4'] = Armor[21] 
                elif inventorySlot == 7:
                    current_state['Additional5'] = Armor[21]
        elif 450 < mouseX < 600 and 540 < mouseY < 560:
            background(139,0,0)
            if currentChoices == Items:
                if inventorySlot == 1:
                    current_state['Equipped1'] = Items[22]
                elif inventorySlot == 2:
                    current_state['Equipped2'] = Items[22]
                elif inventorySlot == 3:
                    current_state['Equipped3'] = Items[22]
                elif inventorySlot == 4:
                    current_state['Additional1'] = Items[22]
                elif inventorySlot == 5:
                    current_state['Additional2'] = Items[22]
                elif inventorySlot == 6:
                    current_state['Additional3'] = Items[22]
                elif inventorySlot == 7:
                    current_state['Additional4'] = Items[22] 
                elif inventorySlot == 8:
                    current_state['Additional5'] = Items[22]
            elif currentChoices == Weapons:
                if inventorySlot == 1:
                    current_state['Equipped1'] = Weapons[22]
                elif inventorySlot == 2:
                    current_state['Equipped2'] = Weapons[22]
                elif inventorySlot == 3:
                    current_state['Equipped3'] = Weapons[22]
                elif inventorySlot == 3:
                    current_state['Additional1'] = Weapons[22]
                elif inventorySlot == 4:
                    current_state['Additional2'] = Weapons[22]
                elif inventorySlot == 5:
                    current_state['Additional3'] = Weapons[22]
                elif inventorySlot == 6:
                    current_state['Additional4'] = Weapons[22] 
                elif inventorySlot == 7:
                    current_state['Additional5'] = Weapons[22]
            elif currentChoices == Armor:
                if inventorySlot == 1:
                    current_state['Equipped1'] = Armor[22]
                elif inventorySlot == 2:
                    current_state['Equipped2'] = Armor[22]
                elif inventorySlot == 3:
                    current_state['Equipped3'] = Armor[22]
                elif inventorySlot == 3:
                    current_state['Additional1'] = Armor[22]
                elif inventorySlot == 4:
                    current_state['Additional2'] = Armor[22]
                elif inventorySlot == 5:
                    current_state['Additional3'] = Armor[22]
                elif inventorySlot == 6:
                    current_state['Additional4'] = Armor[22] 
                elif inventorySlot == 7:
                    current_state['Additional5'] = Armor[22]
        elif 450 < mouseX < 600 and 560 < mouseY < 580:
            background(139,0,0)
            if currentChoices == Items:
                if inventorySlot == 1:
                    current_state['Equipped1'] = Items[23]
                elif inventorySlot == 2:
                    current_state['Equipped2'] = Items[23]
                elif inventorySlot == 3:
                    current_state['Equipped3'] = Items[23]
                elif inventorySlot == 4:
                    current_state['Additional1'] = Items[23]
                elif inventorySlot == 5:
                    current_state['Additional2'] = Items[23]
                elif inventorySlot == 6:
                    current_state['Additional3'] = Items[23]
                elif inventorySlot == 7:
                    current_state['Additional4'] = Items[23] 
                elif inventorySlot == 8:
                    current_state['Additional5'] = Items[23]
            elif currentChoices == Weapons:
                if inventorySlot == 1:
                    current_state['Equipped1'] = Weapons[23]
                elif inventorySlot == 2:
                    current_state['Equipped2'] = Weapons[23]
                elif inventorySlot == 3:
                    current_state['Equipped3'] = Weapons[23]
                elif inventorySlot == 3:
                    current_state['Additional1'] = Weapons[23]
                elif inventorySlot == 4:
                    current_state['Additional2'] = Weapons[23]
                elif inventorySlot == 5:
                    current_state['Additional3'] = Weapons[23]
                elif inventorySlot == 6:
                    current_state['Additional4'] = Weapons[23] 
                elif inventorySlot == 7:
                    current_state['Additional5'] = Weapons[23]
            elif currentChoices == Armor:
                if inventorySlot == 1:
                    current_state['Equipped1'] = Armor[23]
                elif inventorySlot == 2:
                    current_state['Equipped2'] = Armor[23]
                elif inventorySlot == 3:
                    current_state['Equipped3'] = Armor[23]
                elif inventorySlot == 3:
                    current_state['Additional1'] = Armor[23]
                elif inventorySlot == 4:
                    current_state['Additional2'] = Armor[23]
                elif inventorySlot == 5:
                    current_state['Additional3'] = Armor[23]
                elif inventorySlot == 6:
                    current_state['Additional4'] = Armor[23] 
                elif inventorySlot == 7:
                    current_state['Additional5'] = Armor[23]
        elif 600 < mouseX < 750 and 100 < mouseY < 120:
            background(139,0,0)
            if currentChoices == Items:
                if inventorySlot == 1:
                    current_state['Equipped1'] = Items[24]
                elif inventorySlot == 2:
                    current_state['Equipped2'] = Items[24]
                elif inventorySlot == 3:
                    current_state['Equipped3'] = Items[24]
                elif inventorySlot == 4:
                    current_state['Additional1'] = Items[24]
                elif inventorySlot == 5:
                    current_state['Additional2'] = Items[24]
                elif inventorySlot == 6:
                    current_state['Additional3'] = Items[24]
                elif inventorySlot == 7:
                    current_state['Additional4'] = Items[24] 
                elif inventorySlot == 8:
                    current_state['Additional5'] = Items[24]
            elif currentChoices == Weapons:
                if inventorySlot == 1:
                    current_state['Equipped1'] = Weapons[24]
                elif inventorySlot == 2:
                    current_state['Equipped2'] = Weapons[24]
                elif inventorySlot == 3:
                    current_state['Equipped3'] = Weapons[24]
                elif inventorySlot == 3:
                    current_state['Additional1'] = Weapons[24]
                elif inventorySlot == 4:
                    current_state['Additional2'] = Weapons[24]
                elif inventorySlot == 5:
                    current_state['Additional3'] = Weapons[24]
                elif inventorySlot == 6:
                    current_state['Additional4'] = Weapons[24] 
                elif inventorySlot == 7:
                    current_state['Additional5'] = Weapons[24]
        elif 600 < mouseX < 750 and 120 < mouseY < 140:
            background(139,0,0)
            if currentChoices == Items:
                if inventorySlot == 1:
                    current_state['Equipped1'] = Items[25]
                elif inventorySlot == 2:
                    current_state['Equipped2'] = Items[25]
                elif inventorySlot == 3:
                    current_state['Equipped3'] = Items[25]
                elif inventorySlot == 4:
                    current_state['Additional1'] = Items[25]
                elif inventorySlot == 5:
                    current_state['Additional2'] = Items[25]
                elif inventorySlot == 6:
                    current_state['Additional3'] = Items[25]
                elif inventorySlot == 7:
                    current_state['Additional4'] = Items[25] 
                elif inventorySlot == 8:
                    current_state['Additional5'] = Items[25]
            elif currentChoices == Weapons:
                if inventorySlot == 1:
                    current_state['Equipped1'] = Weapons[25]
                elif inventorySlot == 2:
                    current_state['Equipped2'] = Weapons[25]
                elif inventorySlot == 3:
                    current_state['Equipped3'] = Weapons[25]
                elif inventorySlot == 3:
                    current_state['Additional1'] = Weapons[25]
                elif inventorySlot == 4:
                    current_state['Additional2'] = Weapons[25]
                elif inventorySlot == 5:
                    current_state['Additional3'] = Weapons[25]
                elif inventorySlot == 6:
                    current_state['Additional4'] = Weapons[25] 
                elif inventorySlot == 7:
                    current_state['Additional5'] = Weapons[25]
        elif 600 < mouseX < 750 and 140 < mouseY < 160:
            background(139,0,0)
            if currentChoices == Items:
                if inventorySlot == 1:
                    current_state['Equipped1'] = Items[26]
                elif inventorySlot == 2:
                    current_state['Equipped2'] = Items[26]
                elif inventorySlot == 3:
                    current_state['Equipped3'] = Items[26]
                elif inventorySlot == 4:
                    current_state['Additional1'] = Items[26]
                elif inventorySlot == 5:
                    current_state['Additional2'] = Items[26]
                elif inventorySlot == 6:
                    current_state['Additional3'] = Items[26]
                elif inventorySlot == 7:
                    current_state['Additional4'] = Items[26] 
                elif inventorySlot == 8:
                    current_state['Additional5'] = Items[26]
            elif currentChoices == Weapons:
                if inventorySlot == 1:
                    current_state['Equipped1'] = Weapons[26]
                elif inventorySlot == 2:
                    current_state['Equipped2'] = Weapons[26]
                elif inventorySlot == 3:
                    current_state['Equipped3'] = Weapons[26]
                elif inventorySlot == 3:
                    current_state['Additional1'] = Weapons[26]
                elif inventorySlot == 4:
                    current_state['Additional2'] = Weapons[26]
                elif inventorySlot == 5:
                    current_state['Additional3'] = Weapons[26]
                elif inventorySlot == 6:
                    current_state['Additional4'] = Weapons[26] 
                elif inventorySlot == 7:
                    current_state['Additional5'] = Weapons[26]
        elif 600 < mouseX < 750 and 160 < mouseY < 180:
            background(139,0,0)
            if currentChoices == Items:
                if inventorySlot == 1:
                    current_state['Equipped1'] = Items[27]
                elif inventorySlot == 2:
                    current_state['Equipped2'] = Items[27]
                elif inventorySlot == 3:
                    current_state['Equipped3'] = Items[27]
                elif inventorySlot == 4:
                    current_state['Additional1'] = Items[27]
                elif inventorySlot == 5:
                    current_state['Additional2'] = Items[27]
                elif inventorySlot == 6:
                    current_state['Additional3'] = Items[27]
                elif inventorySlot == 7:
                    current_state['Additional4'] = Items[27] 
                elif inventorySlot == 8:
                    current_state['Additional5'] = Items[27]
            elif currentChoices == Weapons:
                if inventorySlot == 1:
                    current_state['Equipped1'] = Weapons[27]
                elif inventorySlot == 2:
                    current_state['Equipped2'] = Weapons[27]
                elif inventorySlot == 3:
                    current_state['Equipped3'] = Weapons[27]
                elif inventorySlot == 3:
                    current_state['Additional1'] = Weapons[27]
                elif inventorySlot == 4:
                    current_state['Additional2'] = Weapons[27]
                elif inventorySlot == 5:
                    current_state['Additional3'] = Weapons[27]
                elif inventorySlot == 6:
                    current_state['Additional4'] = Weapons[27] 
                elif inventorySlot == 7:
                    current_state['Additional5'] = Weapons[27]
        elif 600 < mouseX < 750 and 180 < mouseY < 200:
            background(139,0,0)
            if currentChoices == Items:
                if inventorySlot == 1:
                    current_state['Equipped1'] = Items[28]
                elif inventorySlot == 2:
                    current_state['Equipped2'] = Items[28]
                elif inventorySlot == 3:
                    current_state['Equipped3'] = Items[28]
                elif inventorySlot == 4:
                    current_state['Additional1'] = Items[28]
                elif inventorySlot == 5:
                    current_state['Additional2'] = Items[28]
                elif inventorySlot == 6:
                    current_state['Additional3'] = Items[28]
                elif inventorySlot == 7:
                    current_state['Additional4'] = Items[28] 
                elif inventorySlot == 8:
                    current_state['Additional5'] = Items[28]
            elif currentChoices == Weapons:
                if inventorySlot == 1:
                    current_state['Equipped1'] = Weapons[28]
                elif inventorySlot == 2:
                    current_state['Equipped2'] = Weapons[28]
                elif inventorySlot == 3:
                    current_state['Equipped3'] = Weapons[28]
                elif inventorySlot == 3:
                    current_state['Additional1'] = Weapons[28]
                elif inventorySlot == 4:
                    current_state['Additional2'] = Weapons[28]
                elif inventorySlot == 5:
                    current_state['Additional3'] = Weapons[28]
                elif inventorySlot == 6:
                    current_state['Additional4'] = Weapons[28] 
                elif inventorySlot == 7:
                    current_state['Additional5'] = Weapons[28]
        elif 600 < mouseX < 750 and 200 < mouseY < 220:
            background(139,0,0)
            if currentChoices == Items:
                if inventorySlot == 1:
                    current_state['Equipped1'] = Items[29]
                elif inventorySlot == 2:
                    current_state['Equipped2'] = Items[29]
                elif inventorySlot == 3:
                    current_state['Equipped3'] = Items[29]
                elif inventorySlot == 4:
                    current_state['Additional1'] = Items[29]
                elif inventorySlot == 5:
                    current_state['Additional2'] = Items[29]
                elif inventorySlot == 6:
                    current_state['Additional3'] = Items[29]
                elif inventorySlot == 7:
                    current_state['Additional4'] = Items[29] 
                elif inventorySlot == 8:
                    current_state['Additional5'] = Items[29]
            elif currentChoices == Weapons:
                if inventorySlot == 1:
                    current_state['Equipped1'] = Weapons[29]
                elif inventorySlot == 2:
                    current_state['Equipped2'] = Weapons[29]
                elif inventorySlot == 3:
                    current_state['Equipped3'] = Weapons[29]
                elif inventorySlot == 3:
                    current_state['Additional1'] = Weapons[29]
                elif inventorySlot == 4:
                    current_state['Additional2'] = Weapons[29]
                elif inventorySlot == 5:
                    current_state['Additional3'] = Weapons[29]
                elif inventorySlot == 6:
                    current_state['Additional4'] = Weapons[29] 
                elif inventorySlot == 7:
                    current_state['Additional5'] = Weapons[29]
        elif 600 < mouseX < 750 and 220 < mouseY < 240:
            background(139,0,0)
            if currentChoices == Items:
                if inventorySlot == 1:
                    current_state['Equipped1'] = Items[30]
                elif inventorySlot == 2:
                    current_state['Equipped2'] = Items[30]
                elif inventorySlot == 3:
                    current_state['Equipped3'] = Items[30]
                elif inventorySlot == 4:
                    current_state['Additional1'] = Items[30]
                elif inventorySlot == 5:
                    current_state['Additional2'] = Items[30]
                elif inventorySlot == 6:
                    current_state['Additional3'] = Items[30]
                elif inventorySlot == 7:
                    current_state['Additional4'] = Items[30] 
                elif inventorySlot == 8:
                    current_state['Additional5'] = Items[30]
            elif currentChoices == Weapons:
                if inventorySlot == 1:
                    current_state['Equipped1'] = Weapons[30]
                elif inventorySlot == 2:
                    current_state['Equipped2'] = Weapons[30]
                elif inventorySlot == 3:
                    current_state['Equipped3'] = Weapons[30]
                elif inventorySlot == 3:
                    current_state['Additional1'] = Weapons[30]
                elif inventorySlot == 4:
                    current_state['Additional2'] = Weapons[30]
                elif inventorySlot == 5:
                    current_state['Additional3'] = Weapons[30]
                elif inventorySlot == 6:
                    current_state['Additional4'] = Weapons[30] 
                elif inventorySlot == 7:
                    current_state['Additional5'] = Weapons[30]
        elif 600 < mouseX < 750 and 240 < mouseY < 260:
            background(139,0,0)
            if currentChoices == Items:
                if inventorySlot == 1:
                    current_state['Equipped1'] = Items[31]
                elif inventorySlot == 2:
                    current_state['Equipped2'] = Items[31]
                elif inventorySlot == 3:
                    current_state['Equipped3'] = Items[31]
                elif inventorySlot == 4:
                    current_state['Additional1'] = Items[31]
                elif inventorySlot == 5:
                    current_state['Additional2'] = Items[31]
                elif inventorySlot == 6:
                    current_state['Additional3'] = Items[31]
                elif inventorySlot == 7:
                    current_state['Additional4'] = Items[31] 
                elif inventorySlot == 8:
                    current_state['Additional5'] = Items[31]
        elif 600 < mouseX < 750 and 260 < mouseY < 280:
            background(139,0,0)
            if currentChoices == Items:
                if inventorySlot == 1:
                    current_state['Equipped1'] = Items[32]
                elif inventorySlot == 2:
                    current_state['Equipped2'] = Items[32]
                elif inventorySlot == 3:
                    current_state['Equipped3'] = Items[32]
                elif inventorySlot == 4:
                    current_state['Additional1'] = Items[32]
                elif inventorySlot == 5:
                    current_state['Additional2'] = Items[32]
                elif inventorySlot == 6:
                    current_state['Additional3'] = Items[32]
                elif inventorySlot == 7:
                    current_state['Additional4'] = Items[32] 
                elif inventorySlot == 8:
                    current_state['Additional5'] = Items[32]
        elif 600 < mouseX < 750 and 280 < mouseY < 300:
            background(139,0,0)
            if currentChoices == Items:
                if inventorySlot == 1:
                    current_state['Equipped1'] = Items[33]
                elif inventorySlot == 2:
                    current_state['Equipped2'] = Items[33]
                elif inventorySlot == 3:
                    current_state['Equipped3'] = Items[33]
                elif inventorySlot == 4:
                    current_state['Additional1'] = Items[33]
                elif inventorySlot == 5:
                    current_state['Additional2'] = Items[33]
                elif inventorySlot == 6:
                    current_state['Additional3'] = Items[33]
                elif inventorySlot == 7:
                    current_state['Additional4'] = Items[33] 
                elif inventorySlot == 8:
                    current_state['Additional5'] = Items[33]
        elif 600 < mouseX < 750 and 300 < mouseY < 320:
            background(139,0,0)
            if currentChoices == Items:
                if inventorySlot == 1:
                    current_state['Equipped1'] = Items[34]
                elif inventorySlot == 2:
                    current_state['Equipped2'] = Items[34]
                elif inventorySlot == 3:
                    current_state['Equipped3'] = Items[34]
                elif inventorySlot == 4:
                    current_state['Additional1'] = Items[34]
                elif inventorySlot == 5:
                    current_state['Additional2'] = Items[34]
                elif inventorySlot == 6:
                    current_state['Additional3'] = Items[34]
                elif inventorySlot == 7:
                    current_state['Additional4'] = Items[34] 
                elif inventorySlot == 8:
                    current_state['Additional5'] = Items[34]
        
def playerChoice(): #Makes the player screen buttons clickable  
    global currentplayer
    global current_state
    global choicePopupActive
    if mousePressed:
        if 0 < mouseX < 100 and 0 < mouseY < 35:
            currentplayer = 1
            current_state = player_one
            background(139,0,0)
            choicePopupActive = False
        elif 100 < mouseX < 200 and 0 < mouseY < 35:
            currentplayer = 2
            current_state = player_two
            background(139,0,0)
            choicePopupActive = False
        elif 200 < mouseX < 300 and 0 < mouseY < 35:
            currentplayer = 3
            current_state = player_three
            background(139,0,0)
            choicePopupActive = False
        elif 300 < mouseX < 400 and 0 < mouseY < 35:
            currentplayer = 4
            current_state = player_four
            background(139,0,0)
            choicePopupActive = False
        elif 400 < mouseX < 500 and 0 < mouseY < 35:
            currentplayer = 5
            current_state = player_five
            background(139,0,0)
            choicePopupActive = False
        elif 500 < mouseX < 600 and 0 < mouseY < 35:
            currentplayer = 6
            current_state = player_six
            background(139,0,0)
            choicePopupActive = False
        elif 600 < mouseX < 700 and 0 < mouseY < 35:
            currentplayer = 7
            current_state = player_seven
            background(139,0,0)
            choicePopupActive = False
        elif 700 < mouseX < 800 and 0 < mouseY < 35:
            currentplayer = 8
            current_state = player_eight
            background(139,0,0)
            choicePopupActive = False
        
def fullReset(): #Resets everything back to the base state when BACKSPACE has been pressed
    global player_one
    global player_two
    global player_three
    global player_four
    global player_five
    global player_six
    global player_seven
    global player_eight
    global current_state
    global currentChoices
    global choicePopupActive
    global inventorySlot
    if keyPressed:
        if key == BACKSPACE:
            background(139,0,0)
            player_one = {'Equipped1': 'Empty', 'Equipped2': 'Empty', 'Equipped3': 'Empty', 'Additional1': 'Empty', 'Additional2': 'Empty', 'Additional3': 'Empty',  'Additional4': 'Empty',  'Additional5': 'Empty'}
            player_two = {'Equipped1': 'Empty', 'Equipped2': 'Empty', 'Equipped3': 'Empty', 'Additional1': 'Empty', 'Additional2': 'Empty', 'Additional3': 'Empty',  'Additional4': 'Empty',  'Additional5': 'Empty'}
            player_three = {'Equipped1': 'Empty', 'Equipped2': 'Empty', 'Equipped3': 'Empty', 'Additional1': 'Empty', 'Additional2': 'Empty', 'Additional3': 'Empty',  'Additional4': 'Empty',  'Additional5': 'Empty'}
            player_four = {'Equipped1': 'Empty', 'Equipped2': 'Empty', 'Equipped3': 'Empty', 'Additional1': 'Empty', 'Additional2': 'Empty', 'Additional3': 'Empty',  'Additional4': 'Empty',  'Additional5': 'Empty'}
            player_five = {'Equipped1': 'Empty', 'Equipped2': 'Empty', 'Equipped3': 'Empty', 'Additional1': 'Empty', 'Additional2': 'Empty', 'Additional3': 'Empty',  'Additional4': 'Empty',  'Additional5': 'Empty'}
            player_six = {'Equipped1': 'Empty', 'Equipped2': 'Empty', 'Equipped3': 'Empty', 'Additional1': 'Empty', 'Additional2': 'Empty', 'Additional3': 'Empty',  'Additional4': 'Empty',  'Additional5': 'Empty'}
            player_seven = {'Equipped1': 'Empty', 'Equipped2': 'Empty', 'Equipped3': 'Empty', 'Additional1': 'Empty', 'Additional2': 'Empty', 'Additional3': 'Empty',  'Additional4': 'Empty',  'Additional5': 'Empty'}
            player_eight = {'Equipped1': 'Empty', 'Equipped2': 'Empty', 'Equipped3': 'Empty', 'Additional1': 'Empty', 'Additional2': 'Empty', 'Additional3': 'Empty',  'Additional4': 'Empty',  'Additional5': 'Empty'}
            current_state = player_one
            currentChoices = Items
            choicePopupActive = False
            inventorySlot = 1
            
