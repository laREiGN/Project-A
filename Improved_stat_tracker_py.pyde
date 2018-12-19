'''
State 3
Stat Tracker
Groep 5, Tyron, Girts, Bastiaan, 2018
'''

import textwrap


## Initialization ##

SETUP_NAME = ''
SETUP_MAX_HP = 0
SETUP_STR = 1
SETUP_INT = 1
SETUP_DEX = 1
SETUP_AGI = 1
SETUP_STATUS = []
SETUP_SPELLS = []
SETUP_EQUIPMENT = {}
SETUP_INVENTORY = {}
SETUP_CLASS_ABILITY = {}
SETUP_HERO_CLASS = ''

limit_break_str = False
limit_break_dex = False
limit_break_int = False
limit_break_agi = False

warrior = False
wizard = False
saint = False
monk = False
ranger = False
warlock = False
rogue = False
paladin = True

state = 3
turns = 0
global_turns = 0
players = 2
curr_char = []
char_in_list = ['Tyron', 'Bastiaan']

paladinimg = 0

base_items_stats = {
               'item_name': 'unknown', 
               'max_hp': SETUP_MAX_HP, 
               'hp': SETUP_MAX_HP, 
               'str': SETUP_STR, 
               'int': SETUP_INT, 
               'dex': SETUP_DEX, 
               'agi': SETUP_AGI
               }

base_player_stats = {
                'name': 'unknown', 
                'class' : 'unknown', 
                'max_hp': SETUP_MAX_HP, 
                'hp': SETUP_MAX_HP, 
                'str': SETUP_STR, 
                'int': SETUP_INT, 
                'dex': SETUP_DEX, 
                'agi': SETUP_AGI,
                'status': ['Fit'],
                'equipment': ['Empty'], 
                'spells': ['Empty'],
                'inventory': ['Empty'],
                }

## Main Stat Handling ##

class Player:
    '''Initialized state for every new player that enters the game via character assignment, inventory and equipment are not visible for the user but are still being tracked.'''
    def __init__(self, SETUP_NAME):
        self.name = SETUP_NAME
        self.hero_class = SETUP_HERO_CLASS
        self.max_hp = SETUP_MAX_HP
        self.current_hp = self.max_hp
        self.stat_str = SETUP_STR
        self.dex = SETUP_DEX
        self.agi = SETUP_AGI
        self.stat_int = SETUP_INT
        self.status = SETUP_STATUS
        self.spells = SETUP_SPELLS
        self.equipment = SETUP_EQUIPMENT
        self.inventory = SETUP_INVENTORY
        self.class_ability = SETUP_CLASS_ABILITY
        
# Stat Addition/Substraction Methods #
    
    def inc_hp(self, amount):
        '''Method that increases the of a hero hp by an arbitrary amount, up to max hp.'''
        self.hp += amount
        if self.current_hp > self.max_hp:
            self.current_hp = self.max_hp
    
    def inc_str(self, amount):
        '''Method that increases the strength of the hero by an arbitrary amount, if limit break for strength is active the hero can limit break their stat.'''
        self.stat_str += amount
        if limit_break_str == True:
            self.stat_str = 6
            if self.stat_str > 5:
                self.stat_str = 6
        elif self.stat_str > 5:
            self.stat_str = 5

    def inc_dex(self, amount):
        '''Method that increases the dexterity of the hero by an arbitrary amount, if limit break for dexterity is active the hero can limit break their stat.'''
        self.dex += amount
        if limit_break_dex == True:
            self.dex = 6
            if self.dex > 5:
                self.dex = 6
        elif self.dex > 5:
            self.dex = 5
    
    def inc_int(self, amount):
        '''Method that increases the intelligence of the hero by an arbitrary amount, if limit break for intelligence is active the hero can limit break their stat.'''
        self.stat_int += amount
        if limit_break_int == True:
            self.stat_int = 6
            if self.stat_int > 5:
                self.stat_int = 6
        elif self.stat_int > 5:
            self.stat_int = 5
   
    def inc_agi(self, amount):
        '''Method that increases the agility of the hero by an arbitrary amount, if limit break for agility is active the hero can limit break their stat.'''
        self.agi += amount
        if limit_break_agi == True:
            self.agi = 6
            if self.agi > 5:
                self.agi = 6
        elif self.agi > 5:
            self.agi = 5
    
    def decr_hp(self, amount):
        '''Method that decreases health of a hero when called with an arbitrary amount.'''
        self.current_hp -= amount
        if self.current_hp < 0:
            self.current_hp = 0
    
    def decr_str(self, amount):
        self.stat_str -= amount
        if self.stat_str <= 0:
            self.stat_str = 1
            
    def decr_dex(self, amount):
        self.dex -= amount
        if self.dex <= 0:
            self.dex = 1
            
    def decr_int(self, amount):
        self.stat_int -= amount
        if self.stat_int <= 0:
            self.stat_int = 1
            
    def decr_agi(self, amount):
        self.agi -= amount
        if self.agi <= 0:
            self.agi = 1
            
# Hero Class Assigment Methods #
            
    def assign_warrior(self):
        if warrior == True:
            self.hero_class = 'Warrior'
            self.max_hp = 25
            self.stat_str = 5
            self.dex = 2
            self.agi = 2
            self.stat_int = 1
            self.status = 'Fit'
            self.class_ability['The Sound of Fear'] =  "When used, any damage done to a different player gets directed to the warrior." \n 
            "A temporaily hp bonus equal to half the Warrior's maximum health for the entire battle and pulls aggro regardless of when they attacked for 1 turn" \n 
            "(this bonus stacks with your current health)."
    
    def assign_saint(self):
        if saint == True:
            self.hero_class = 'Saint'
            self.max_hp = 25
            self.stat_str = 1
            self.dex = 3
            self.agi = 3
            self.stat_int = 5
            self.status = 'Fit'
            self.class_ability['Divine Blessing'] = 'When the Saint uses a healing type spell they can make the effects party wide' \n 
            'for as long as the group is fighting within the same encounter, or on the same space.'
            self.spells.append('Recover')
            
    def assign_wizard(self):
        if wizard == True:
            self.hero_class = 'Wizard'
            self.max_hp = 10
            self.stat_str = 5
            self.dex = 2
            self.agi = 2
            self.stat_int = 1
            self.class_abilty['Arcane Expetise'] = 'The Wizard is capable of learning any spell, with its cooldown being equal to its rarity,' \n
            '(magic missile no cooldown, uncommon 2 battles, rare 3 battles, legendary 4 battles, The Wizard cannot learn resurection magic.)'
            self.spells.append('Magic Missile')
            self.status = 'Fit'
            
    def assign_warlock(self):
        if warlock == True:
            self.hero_class = 'Warlock'
            self.max_hp = 15
            self.stat_str = 2
            self.dex = 2
            self.agi = 3
            self.stat_int = 5
            self.status.append('Fit')
            self.class_ability['Intertwine Fate'] = 'The Warlock can bind a creature of Uncommon or lower ranking to the Warlock.' \n 
            'The creature will be decided by drawing monsters from the monster pile until a common or uncommon monster card is drawn.' \n 
            'The creature and Warlock are bound by life, when the creature dies the Warlock receives damage depending on the ranking of the monster (Common = 5 damage, Uncommon = 10 damage).' \n 
            "The creature acts directly after the Warlock's turn. The warlock can summon another creature if their current creature has died, but with every summoned creature's death, the damage penalty for a creature dying will increase by 2."
            
    def assign_rogue(self):
        if rogue == True:
            self.hero_class = 'Rogue'
            self.max_hp = 15
            self.stat_str = 2
            self.dex = 3
            self.agi = 5
            self.stat_int = 2
            self.class_ability['Assassinate'] = "When the Rogue is faster than its opponent they deal a preemptive strike on the turn they join the combat instead of doing their normal attack. The damage is equal to the rogue's weapon damage, plus AGI + DEX."
            self.status.append('Fit')
            
    def assign_paladin(self):
        if paladin == True:
            self.hero_class = 'Paladin'
            self.max_hp = 20
            self.stat_str = 4
            self.dex = 1
            self.agi = 2
            self.stat_int = 4
            self.class_ability['Empower Weapon'] = 'At any point in combat the Paladin can imbue their weapon with the sacred magic from they know from the start of the game to give their next attack a special effect, specified on the spell card.' \n
            'Also damage is calculated as weapon power + intelligence for one attack, (Has a cooldown of 2 turns).'
            self.status.append('Fit')
            self.spells.append('Shine', 'Blessed Touch', 'Grant Blessing')
            
    def assign_ranger(self):
        if ranger == True:
            self.hero_class = 'Ranger'
            self.max_hp = 25
            self.stat_str = 1
            self.dex = 5
            self.agi = 4
            self.stat_int = 2
            self.class_ability['Snipe'] = "If the Ranger is two spaces away from an encounter the Ranger hasn't started, they can join combat from two spaces away." \n 
            "If the player that generated the encounter dies, the encounter shifts from the dead player to the ranger, and the encounter will start attacking after a 1 turn delay." \n 
            '(this class ability can only be used if the Ranger posseses a DEX-Based Ranged weapon).'
            self.status.append('Fit')
    
    def assign_monk(self):
        if monk == True:
            self.hero_class = 'Monk'
            self.max_hp = 15
            self.stat_str = 2
            self.dex = 4
            self.agi = 4
            self.stat_int = 2
            self.status.append('Fit')
            self.class_ability['Taoism'] = "At any point in combat the Monk can make two attacks in one turn, the standard dealing 100% damage and the second strike at half damage value of the first strike." \n
            "This ability isn't usable when the Monk is using a two handed weapon, (Has a cooldown of 3 turns)."
            
    def print_stats(self):
        print ('My health is: ' + str(self.current_hp) + ' / ' + str(self.max_hp))

## Player Handling ##

pl1 = Player('Tyron')
pl1.assign_warrior()
        
## Item Handling ##


## UI ##

def setup():
    '''Sets up the background color, screensize and fills it with color.'''
# General Layout #
    
    background(139,0,0)
    size(1500, 800)
    fill(218,165,32)
    rect(75, 25, 450, 750)
    rect(550, 525, 850, 200)
    fill(255)
    
# Stat Adjustment Buttons #
    
    rect(540, 125, 50, 35)
    rect(700, 125, 50, 35)
    rect(540, 175, 50, 35)
    rect(700, 175, 50, 35)
    rect(540, 225, 50, 35)
    rect(700, 225, 50, 35)
    rect(540, 275, 50, 35)
    rect(700, 275, 50, 35)
    rect(540, 325, 50, 35)
    rect(700, 325, 50, 35)
    rect(540, 375, 50, 35)
    rect(700, 375, 50, 35)
    rect(540, 425, 50, 35)
    rect(775, 425, 50, 35)
    rect(615, 125, 65, 35)
    rect(615, 175, 65, 35)
    rect(615, 225, 65, 35)
    rect(615, 275, 65, 35)
    rect(615, 325, 65, 35)
    rect(615, 375, 65, 35)
    rect(615, 425, 135, 35)
    
# Spells and Class Ability Screen #
    
    fill(255)
    rect(100, 505, 400, 250)
    line(100, 550, 500, 550)
    rect(560, 550, 825, 150)
    line(560, 590, 900, 590)
    line(900, 590, 900, 550)
    
# Update and Back Buttons #
    
    fill(218,165,32)
    rect(1125, 745, 125, 50)
    rect(1275, 745, 125, 50)
    
    
def mouse_press():
    pass
    
def load_images():
    '''Function that deals with displaying and managing class card images within the program.'''
    global warriorimg
    global saintimg
    global wizardimg
    global monkimg
    global rangerimg
    global warlockimg
    global paladinimg
    global rogueimg
    paladinimg = loadImage('paladin.png')
    image(paladinimg, 0, 0, 320, 500)
# Image Positioning


def draw_unmutable_text():
    '''Draws all unmutable text in the program.'''
    textSize(32)
    fill(0)
    text('-', 715, 153)
    text('-', 715, 203)
    text('-', 715, 253)
    text('-', 715, 303)
    text('-', 715, 353)
    text('-', 715, 403)
    text('-', 790, 453)
    text('+', 553, 153)
    text('+', 553, 203)
    text('+', 553, 253)
    text('+', 553, 303)
    text('+', 553, 353)
    text('+', 553, 403)
    text('+', 553, 453)
    textSize(17)
    text('Name: ', 330, 60)
    text('Class: ', 330, 100)
    text('HP: ', 330, 153)
    text('Max HP: ', 330, 203)
    text('Strength: ', 330, 253)
    text('Dexterity: ', 330, 303)
    text('Agility: ', 330, 353)
    text('Intelligence: ', 330, 403)
    text('Status: ', 330, 453)
    textSize(20)
    text('Class Ability', 670, 577) 
    text('Spells', 275, 535)
    text('Update', 1155, 778)
    text('Back', 1315, 778)
    
def draw_mutable_text():
    '''Draws all mutable text within the program, using 'x' as it's parameter.'''
    textSize(15)
    text(str(pl1.name), 450, 60)
    text(str(pl1.hero_class), 450, 100)
    text(str(pl1.current_hp), 470, 153)
    text(str(pl1.max_hp), 470, 203)
    text(str(pl1.stat_str), 470, 253)
    text(str(pl1.dex), 470, 303)
    text(str(pl1.agi), 470, 353)
    text(str(pl1.stat_int), 470, 403)
    text(str(pl1.status), 470, 453) 
    if len(pl1.spells) > 1:
        text(wrap(str(pl1.spells), 16), 200, 600)

def draw():
    draw_unmutable_text()
    draw_mutable_text()
    load_images()
