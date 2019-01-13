'''
State 3
Stat Tracker
Groep 5, Tyron, Girts, Bastiaan, 2018
'''

## Initialization ##

SETUP_STAT_BASE =  {
                    'class' : 'unknown', 
                    'max_hp': [], 
                    'hp': [], 
                    'str': [], 
                    'int': [], 
                    'dex' : [], 
                    'agi': [], 
                    'status': [], 
                    'damage': [],
                    'class_ability': [],
                    'spells': {},
                    'equipment': {},
                    'inventory': {},
                    'class_ability':{},
                    'limit_break_str': False,
                    'limit_break_dex': False,
                    'limit_break_int': False,
                    'limit_break_agi': False,
                    }

state = 3
turns = 0
global_turns = 0
players = 0
curr_char = 0
final_chars = [('Warrior', 25, 5, 3, 3, 1), ('Wizard', 10, 2, 3, 5, 5), ('Paladin', 20, 5, 1, 2, 5)]

warriorimg = 0
wizardimg = 0
rogueimg = 0
warlockimg = 0
monkimg = 0
saintimg = 0
paladinimg = 0

paladin = False

mouse_x = 0
mouse_y = 0

## Player Handling ##
def player_handling(final_chars, curr_char, pl):
    pl['class'] = final_chars[curr_char][0]
    pl['max_hp'] = final_chars[curr_char][1]
    pl['hp'] = pl1['max_hp']
    pl['str'] = final_chars[curr_char][2]
    pl['dex'] = final_chars[curr_char][3]
    pl['agi'] = final_chars[curr_char][4]
    pl['int'] = final_chars[curr_char][5]
    pl['status'] = 'Fit'
    pl['damage'] = pl1['str'] # needs base weapon damage + dex interaction
        
    if pl['class'] == 'Warrior':
        pl1['class_ability'] = "The Sound of Fear: When used, any damage done to a different player gets directed to the warrior. \n A temporaily hp bonus equal to half the Warrior's maximum health for the entire battle and pulls aggro regardless of when they attacked for 1 turn, \n (this bonus stacks with your current health)."
            
    elif pl['class'] == 'Rogue':
        pl['class_ability'] = "Assassinate: When the Rogue is faster than its opponent they deal a preemptive strike on the turn they join the combat instead of doing their normal attack. The damage is equal to the rogue's weapon damage, plus AGI + DEX."
       
    elif pl['class'] == 'Ranger':
        pl['class_ability'] = "Snipe: If the Ranger is two spaces away from an encounter the Ranger hasn't started, they can join combat from two spaces away." \n 
        "If the player that generated the encounter dies, the encounter shifts from the dead player to the ranger, and the encounter will start attacking after a 1 turn delay." \n 
        '(this class ability can only be used if the Ranger posseses a DEX-Based Ranged weapon).'
        
    elif pl['class'] == 'Monk':
        pl['class_ability'] = "Taoism: At any point in combat the Monk can make two attacks in one turn, the standard dealing 100% damage and the second strike at half damage value of the first strike." \n
        "This ability isn't usable when the Monk is using a two handed weapon, (Has a cooldown of 3 turns)."
        
    elif pl['class'] == 'Warlock':
        pl['class_ability'] = "Intertwine Fate: The Warlock can bind a creature of Uncommon or lower ranking to the Warlock." \n 
        'The creature will be decided by drawing monsters from the monster pile until a common or uncommon monster card is drawn.' \n 
        'The creature and Warlock are bound by life, when the creature dies the Warlock receives damage depending on the ranking of the monster (Common = 5 damage, Uncommon = 10 damage).' \n 
        "The creature acts directly after the Warlock's turn. The warlock can summon another creature if their current creature has died, but with every summoned creature's death, the damage penalty for a creature dying will increase by 2."
            
    elif pl['class'] == 'Wizard':
        pl['spells'].append('Magic Missile')
        pl['class_ability'] = "Arcane Expertise: The Wizard is capable of learning any spell, with its cooldown being equal to its rarity," \n
        '(magic missile no cooldown, uncommon 2 battles, rare 3 battles, legendary 4 battles, The Wizard cannot learn resurection magic.)'
        
    elif pl['class'] == 'Saint':
        pl['spells'].append('Recover')
        pl['class_ability'] = 'Divine Blessing: When the Saint uses a healing type spell they can make the effects party wide' \n 
        'for as long as the group is fighting within the same encounter, or on the same space.'
        
    elif pl['class'] == 'Paladin':
        pl['spells'].extend('Shine', 'Blessed Touch', 'Grant Blessing')

for players in final_chars:
    if len(final_chars) >= 1:
        pl1 = dict(SETUP_STAT_BASE)
        curr_char = 0
        player_handling(final_chars, curr_char, pl1)
    if len(final_chars) >= 2:
        pl2 = dict(SETUP_STAT_BASE)
    if len(final_chars) >= 1:
        pl1 = dict(SETUP_STAT_BASE)
    if len(final_chars) >= 1:
        pl1 = dict(SETUP_STAT_BASE)
        

''' if len(final_chars) >= 2:
        pl2 = dict(SETUP_STAT_BASE)
        pl2['class'] = final_chars[1: 0]
        pl2['max_hp'] = final_chars[1: 1]
        pl2['hp'] = pl1['max_hp']
        pl2['str'] = final_chars[1: 2]
        pl2['dex'] = final_chars[1: 3]
        pl2['agi'] = final_chars[1: 4]
        pl2['int'] = final_chars[1: 5]
        pl2['status'] = 'Fit'
        pl2['damage'] = pl1['str'] # needs base weapon damage + dex interaction
        
        if pl2['class'] == 'Warrior':
            pl2['class_ability'] = "The Sound of Fear: When used, any damage done to a different player gets directed to the warrior." \n 
            "A temporaily hp bonus equal to half the Warrior's maximum health for the entire battle and pulls aggro regardless of when they attacked for 1 turn" \n 
            "(this bonus stacks with your current health)."
            
        elif pl2['class'] == 'Rogue':
            pl2['class_ability'] = "Assassinate: When the Rogue is faster than its opponent they deal a preemptive strike on the turn they join the combat instead of doing their normal attack. The damage is equal to the rogue's weapon damage, plus AGI + DEX."
       
        elif pl2['class'] == 'Ranger':
            pl2['class_ability'] = "Snipe: If the Ranger is two spaces away from an encounter the Ranger hasn't started, they can join combat from two spaces away." \n 
            "If the player that generated the encounter dies, the encounter shifts from the dead player to the ranger, and the encounter will start attacking after a 1 turn delay." \n 
            '(this class ability can only be used if the Ranger posseses a DEX-Based Ranged weapon).'
        
        elif pl2['class'] == 'Monk':
            pl2['class_ability'] = "Taoism: At any point in combat the Monk can make two attacks in one turn, the standard dealing 100% damage and the second strike at half damage value of the first strike." \n
            "This ability isn't usable when the Monk is using a two handed weapon, (Has a cooldown of 3 turns)."
        
        elif pl2['class'] == 'Warlock':
            pl2['class_ability'] = "Intertwine Fate: The Warlock can bind a creature of Uncommon or lower ranking to the Warlock." \n 
            'The creature will be decided by drawing monsters from the monster pile until a common or uncommon monster card is drawn.' \n 
            'The creature and Warlock are bound by life, when the creature dies the Warlock receives damage depending on the ranking of the monster (Common = 5 damage, Uncommon = 10 damage).' \n 
            "The creature acts directly after the Warlock's turn. The warlock can summon another creature if their current creature has died, but with every summoned creature's death, the damage penalty for a creature dying will increase by 2."
            
        elif pl2['class'] == 'Wizard':
            pl2['spells'].append('Magic Missile')
            pl2['class_ability'] = "Arcane Expertise: The Wizard is capable of learning any spell, with its cooldown being equal to its rarity," \n
            '(magic missile no cooldown, uncommon 2 battles, rare 3 battles, legendary 4 battles, The Wizard cannot learn resurection magic.)'
        
        elif pl2['class'] == 'Saint':
            pl2['spells'].append('Recover')
            pl2['class_ability'] = 'Divine Blessing: When the Saint uses a healing type spell they can make the effects party wide' \n 
            'for as long as the group is fighting within the same encounter, or on the same space.'
        
    if len(final_chars) >= 3:
        pl3 = dict(SETUP_STAT_BASE)
        pl3['class'] = final_chars[2: 0]
        pl3['max_hp'] = final_chars[2: 1]
        pl3['hp'] = pl3['max_hp']
        pl3['str'] = final_chars[2: 2]
        pl3['dex'] = final_chars[2: 3]
        pl3['agi'] = final_chars[2: 4]
        pl3['int'] = final_chars[2: 5]
        pl3['status'] = 'Fit'
        pl3['damage'] = pl3['str'] # needs base weapon damage + dex interaction
        
        if pl3['class'] == 'Warrior':
            pl3['class_ability'] = "The Sound of Fear: When used, any damage done to a different player gets directed to the warrior." \n 
            "A temporaily hp bonus equal to half the Warrior's maximum health for the entire battle and pulls aggro regardless of when they attacked for 1 turn" \n 
            "(this bonus stacks with your current health)."
            
        elif pl3['class'] == 'Rogue':
            pl3['class_ability'] = "Assassinate: When the Rogue is faster than its opponent they deal a preemptive strike on the turn they join the combat instead of doing their normal attack. The damage is equal to the rogue's weapon damage, plus AGI + DEX."
       
        elif pl3['class'] == 'Ranger':
            pl3['class_ability'] = "Snipe: If the Ranger is two spaces away from an encounter the Ranger hasn't started, they can join combat from two spaces away." \n 
            "If the player that generated the encounter dies, the encounter shifts from the dead player to the ranger, and the encounter will start attacking after a 1 turn delay." \n 
            '(this class ability can only be used if the Ranger posseses a DEX-Based Ranged weapon).'
        
        elif pl3['class'] == 'Monk':
            pl3['class_ability'] = "Taoism: At any point in combat the Monk can make two attacks in one turn, the standard dealing 100% damage and the second strike at half damage value of the first strike." \n
            "This ability isn't usable when the Monk is using a two handed weapon, (Has a cooldown of 3 turns)."
        
        elif pl3['class'] == 'Warlock':
            pl3['class_ability'] = "Intertwine Fate: The Warlock can bind a creature of Uncommon or lower ranking to the Warlock." \n 
            'The creature will be decided by drawing monsters from the monster pile until a common or uncommon monster card is drawn.' \n 
            'The creature and Warlock are bound by life, when the creature dies the Warlock receives damage depending on the ranking of the monster (Common = 5 damage, Uncommon = 10 damage).' \n 
            "The creature acts directly after the Warlock's turn. The warlock can summon another creature if their current creature has died, but with every summoned creature's death, the damage penalty for a creature dying will increase by 2."
            
        elif pl3['class'] == 'Wizard':
            pl3['spells'].append('Magic Missile')
            pl3['class_ability'] = "Arcane Expertise: The Wizard is capable of learning any spell, with its cooldown being equal to its rarity," \n
            '(magic missile no cooldown, uncommon 2 battles, rare 3 battles, legendary 4 battles, The Wizard cannot learn resurection magic.)'
        
        elif pl3['class'] == 'Saint':
            pl3['spells'].append('Recover')
            pl3['class_ability'] = 'Divine Blessing: When the Saint uses a healing type spell they can make the effects party wide' \n 
            'for as long as the group is fighting within the same encounter, or on the same space.'
        
    if len(final_chars) >= 4:
        pl4 = dict(SETUP_STAT_BASE)
        pl4['class'] = final_chars[3: 0]
        pl4['max_hp'] = final_chars[3: 1]
        pl4['hp'] = pl4['max_hp']
        pl4['str'] = final_chars[3: 2]
        pl4['dex'] = final_chars[3: 3]
        pl4['agi'] = final_chars[3: 4]
        pl4['int'] = final_chars[3: 5]
        pl4['status'] = 'Fit'
        pl4['damage'] = pl4['str'] # needs base weapon damage + dex interaction
        
        if pl4['class'] == 'Warrior':
            pl4['class_ability'] = "The Sound of Fear: When used, any damage done to a different player gets directed to the warrior." \n 
            "A temporaily hp bonus equal to half the Warrior's maximum health for the entire battle and pulls aggro regardless of when they attacked for 1 turn" \n 
            "(this bonus stacks with your current health)."
            
        elif pl4['class'] == 'Rogue':
            pl4['class_ability'] = "Assassinate: When the Rogue is faster than its opponent they deal a preemptive strike on the turn they join the combat instead of doing their normal attack. The damage is equal to the rogue's weapon damage, plus AGI + DEX."
       
        elif pl4['class'] == 'Ranger':
            pl4['class_ability'] = "Snipe: If the Ranger is two spaces away from an encounter the Ranger hasn't started, they can join combat from two spaces away." \n 
            "If the player that generated the encounter dies, the encounter shifts from the dead player to the ranger, and the encounter will start attacking after a 1 turn delay." \n 
            '(this class ability can only be used if the Ranger posseses a DEX-Based Ranged weapon).'
        
        elif pl4['class'] == 'Monk':
            pl4['class_ability'] = "Taoism: At any point in combat the Monk can make two attacks in one turn, the standard dealing 100% damage and the second strike at half damage value of the first strike." \n
            "This ability isn't usable when the Monk is using a two handed weapon, (Has a cooldown of 3 turns)."
        
        elif pl4['class'] == 'Warlock':
            pl4['class_ability'] = "Intertwine Fate: The Warlock can bind a creature of Uncommon or lower ranking to the Warlock." \n 
            'The creature will be decided by drawing monsters from the monster pile until a common or uncommon monster card is drawn.' \n 
            'The creature and Warlock are bound by life, when the creature dies the Warlock receives damage depending on the ranking of the monster (Common = 5 damage, Uncommon = 10 damage).' \n 
            "The creature acts directly after the Warlock's turn. The warlock can summon another creature if their current creature has died, but with every summoned creature's death, the damage penalty for a creature dying will increase by 2."
            
        elif pl4['class'] == 'Wizard':
            pl4['spells'].append('Magic Missile')
            pl4['class_ability'] = "Arcane Expertise: The Wizard is capable of learning any spell, with its cooldown being equal to its rarity," \n
            '(magic missile no cooldown, uncommon 2 battles, rare 3 battles, legendary 4 battles, The Wizard cannot learn resurection magic.)'
        
        elif pl4['class'] == 'Saint':
            pl4['spells'].append('Recover')
            pl4['class_ability'] = 'Divine Blessing: When the Saint uses a healing type spell they can make the effects party wide' \n 
            'for as long as the group is fighting within the same encounter, or on the same space.'
        
    if len(final_chars) >= 5:
        pl5 = dict(SETUP_STAT_BASE)
        pl5['class'] = final_chars[4: 0]
        pl5['max_hp'] = final_chars[4: 1]
        pl5['hp'] = pl5['max_hp']
        pl5['str'] = final_chars[4: 2]
        pl5['dex'] = final_chars[4: 3]
        pl5['agi'] = final_chars[4: 4]
        pl5['int'] = final_chars[4: 5]
        pl5['status'] = 'Fit'
        pl5['damage'] = pl5['str'] # needs base weapon damage + dex interaction
        
        if pl5['class'] == 'Warrior':
            pl5['class_ability'] = "The Sound of Fear: When used, any damage done to a different player gets directed to the warrior." \n 
            "A temporaily hp bonus equal to half the Warrior's maximum health for the entire battle and pulls aggro regardless of when they attacked for 1 turn" \n 
            "(this bonus stacks with your current health)."
            
        elif pl5['class'] == 'Rogue':
            pl5['class_ability'] = "Assassinate: When the Rogue is faster than its opponent they deal a preemptive strike on the turn they join the combat instead of doing their normal attack. The damage is equal to the rogue's weapon damage, plus AGI + DEX."
       
        elif pl5['class'] == 'Ranger':
            pl5['class_ability'] = "Snipe: If the Ranger is two spaces away from an encounter the Ranger hasn't started, they can join combat from two spaces away." \n 
            "If the player that generated the encounter dies, the encounter shifts from the dead player to the ranger, and the encounter will start attacking after a 1 turn delay." \n 
            '(this class ability can only be used if the Ranger posseses a DEX-Based Ranged weapon).'
        
        elif pl5['class'] == 'Monk':
            pl5['class_ability'] = "Taoism: At any point in combat the Monk can make two attacks in one turn, the standard dealing 100% damage and the second strike at half damage value of the first strike." \n
            "This ability isn't usable when the Monk is using a two handed weapon, (Has a cooldown of 3 turns)."
        
        elif pl5['class'] == 'Warlock':
            pl5['class_ability'] = "Intertwine Fate: The Warlock can bind a creature of Uncommon or lower ranking to the Warlock." \n 
            'The creature will be decided by drawing monsters from the monster pile until a common or uncommon monster card is drawn.' \n 
            'The creature and Warlock are bound by life, when the creature dies the Warlock receives damage depending on the ranking of the monster (Common = 5 damage, Uncommon = 10 damage).' \n 
            "The creature acts directly after the Warlock's turn. The warlock can summon another creature if their current creature has died, but with every summoned creature's death, the damage penalty for a creature dying will increase by 2."
            
        elif pl5['class'] == 'Wizard':
            pl5['spells'].append('Magic Missile')
            pl5['class_ability'] = "Arcane Expertise: The Wizard is capable of learning any spell, with its cooldown being equal to its rarity," \n
            '(magic missile no cooldown, uncommon 2 battles, rare 3 battles, legendary 4 battles, The Wizard cannot learn resurection magic.)'
        
        elif pl5['class'] == 'Saint':
            pl5['spells'].append('Recover')
            pl5['class_ability'] = 'Divine Blessing: When the Saint uses a healing type spell they can make the effects party wide' \n 
            'for as long as the group is fighting within the same encounter, or on the same space.'
        
    if len(final_chars) >= 6:
        pl6 = dict(SETUP_STAT_BASE)
        pl6['class'] = final_chars[5: 0]
        pl6['max_hp'] = final_chars[5: 1]
        pl6['hp'] = pl1['max_hp']
        pl6['str'] = final_chars[5: 2]
        pl6['dex'] = final_chars[5: 3]
        pl6['agi'] = final_chars[5: 4]
        pl6['int'] = final_chars[5: 5]
        pl6['status'] = 'Fit'
        pl6['damage'] = pl6['str'] # needs base weapon damage + dex interaction
        
        if pl6['class'] == 'Warrior':
            pl6['class_ability'] = "The Sound of Fear: When used, any damage done to a different player gets directed to the warrior." \n 
            "A temporaily hp bonus equal to half the Warrior's maximum health for the entire battle and pulls aggro regardless of when they attacked for 1 turn" \n 
            "(this bonus stacks with your current health)."
            
        elif pl6['class'] == 'Rogue':
            pl6['class_ability'] = "Assassinate: When the Rogue is faster than its opponent they deal a preemptive strike on the turn they join the combat instead of doing their normal attack. The damage is equal to the rogue's weapon damage, plus AGI + DEX."
       
        elif pl6['class'] == 'Ranger':
            pl6['class_ability'] = "Snipe: If the Ranger is two spaces away from an encounter the Ranger hasn't started, they can join combat from two spaces away." \n 
            "If the player that generated the encounter dies, the encounter shifts from the dead player to the ranger, and the encounter will start attacking after a 1 turn delay." \n 
            '(this class ability can only be used if the Ranger posseses a DEX-Based Ranged weapon).'
        
        elif pl6['class'] == 'Monk':
            pl6['class_ability'] = "Taoism: At any point in combat the Monk can make two attacks in one turn, the standard dealing 100% damage and the second strike at half damage value of the first strike." \n
            "This ability isn't usable when the Monk is using a two handed weapon, (Has a cooldown of 3 turns)."
        
        if pl6['class'] == 'Warlock':
            pl6['class_ability'] = "Intertwine Fate: The Warlock can bind a creature of Uncommon or lower ranking to the Warlock." \n 
            'The creature will be decided by drawing monsters from the monster pile until a common or uncommon monster card is drawn.' \n 
            'The creature and Warlock are bound by life, when the creature dies the Warlock receives damage depending on the ranking of the monster (Common = 5 damage, Uncommon = 10 damage).' \n 
            "The creature acts directly after the Warlock's turn. The warlock can summon another creature if their current creature has died, but with every summoned creature's death, the damage penalty for a creature dying will increase by 2."
            
        elif pl6['class'] == 'Wizard':
            pl6['spells'].append('Magic Missile')
            pl6['class_ability'] = "Arcane Expertise: The Wizard is capable of learning any spell, with its cooldown being equal to its rarity," \n
            '(magic missile no cooldown, uncommon 2 battles, rare 3 battles, legendary 4 battles, The Wizard cannot learn resurection magic.)'
        
        elif pl6['class'] == 'Saint':
            pl6['spells'].append('Recover')
            pl6['class_ability'] = 'Divine Blessing: When the Saint uses a healing type spell they can make the effects party wide' \n 
            'for as long as the group is fighting within the same encounter, or on the same space.'
    
    
    if len(final_chars) >= 7:
        pl7 = dict(SETUP_STAT_BASE)
        pl7['class'] = final_chars[6: 0]
        pl7['max_hp'] = final_chars[6: 1]
        pl7['hp'] = pl7['max_hp']
        pl7['str'] = final_chars[6: 2]
        pl7['dex'] = final_chars[6: 3]
        pl7['agi'] = final_chars[6: 4]
        pl7['int'] = final_chars[6: 5]
        pl7['status'] = 'Fit'
        pl7['damage'] = pl7['str'] # needs base weapon damage + dex interaction
        
        if pl7['class'] == 'Warrior':
            pl7['class_ability'] = "The Sound of Fear: When used, any damage done to a different player gets directed to the warrior." \n 
            "A temporaily hp bonus equal to half the Warrior's maximum health for the entire battle and pulls aggro regardless of when they attacked for 1 turn" \n 
            "(this bonus stacks with your current health)."
            
        if pl7['class'] == 'Rogue':
            pl1['class_ability'] = "Assassinate: When the Rogue is faster than its opponent they deal a preemptive strike on the turn they join the combat instead of doing their normal attack. The damage is equal to the rogue's weapon damage, plus AGI + DEX."
       
        if pl7['class'] == 'Ranger':
            pl7['class_ability'] = "Snipe: If the Ranger is two spaces away from an encounter the Ranger hasn't started, they can join combat from two spaces away." \n 
            "If the player that generated the encounter dies, the encounter shifts from the dead player to the ranger, and the encounter will start attacking after a 1 turn delay." \n 
            '(this class ability can only be used if the Ranger posseses a DEX-Based Ranged weapon).'
        
        if pl7['class'] == 'Monk':
            pl7['class_ability'] = "Taoism: At any point in combat the Monk can make two attacks in one turn, the standard dealing 100% damage and the second strike at half damage value of the first strike." \n
            "This ability isn't usable when the Monk is using a two handed weapon, (Has a cooldown of 3 turns)."
        
        if pl7['class'] == 'Warlock':
            pl7['class_ability'] = "Intertwine Fate: The Warlock can bind a creature of Uncommon or lower ranking to the Warlock." \n 
            'The creature will be decided by drawing monsters from the monster pile until a common or uncommon monster card is drawn.' \n 
            'The creature and Warlock are bound by life, when the creature dies the Warlock receives damage depending on the ranking of the monster (Common = 5 damage, Uncommon = 10 damage).' \n 
            "The creature acts directly after the Warlock's turn. The warlock can summon another creature if their current creature has died, but with every summoned creature's death, the damage penalty for a creature dying will increase by 2."
            
        if pl7['class'] == 'Wizard':
            pl7['spells'].append('Magic Missile')
            pl7['class_ability'] = "Arcane Expertise: The Wizard is capable of learning any spell, with its cooldown being equal to its rarity," \n
            '(magic missile no cooldown, uncommon 2 battles, rare 3 battles, legendary 4 battles, The Wizard cannot learn resurection magic.)'
        
        elif pl7['class'] == 'Saint':
            pl7['spells'].append('Recover')
            pl7['class_ability'] = 'Divine Blessing: When the Saint uses a healing type spell they can make the effects party wide' \n 
            'for as long as the group is fighting within the same encounter, or on the same space.'
        
    if len(final_chars) >= 8:
        pl8 = dict(SETUP_STAT_BASE)
        pl8['class'] = final_chars[7: 0]
        pl8['max_hp'] = final_chars[7: 1]
        pl8['hp'] = pl8['max_hp']
        pl8['str'] = final_chars[7: 2]
        pl8['dex'] = final_chars[7: 3]
        pl8['agi'] = final_chars[7: 4]
        pl8['int'] = final_chars[7: 5]
        pl8['status'] = 'Fit'
        pl8['damage'] = pl8['str'] # needs base weapon damage + dex interaction
        
        if pl8['class'] == 'Warrior':
            pl8['class_ability'] = "The Sound of Fear: When used, any damage done to a different player gets directed to the warrior." \n 
            "A temporaily hp bonus equal to half the Warrior's maximum health for the entire battle and pulls aggro regardless of when they attacked for 1 turn" \n 
            "(this bonus stacks with your current health)."
            
        if pl8['class'] == 'Rogue':
            pl8['class_ability'] = "Assassinate: When the Rogue is faster than its opponent they deal a preemptive strike on the turn they join the combat instead of doing their normal attack. The damage is equal to the rogue's weapon damage, plus AGI + DEX."
       
        if pl8['class'] == 'Ranger':
            pl8['class_ability'] = "Snipe: If the Ranger is two spaces away from an encounter the Ranger hasn't started, they can join combat from two spaces away." \n 
            "If the player that generated the encounter dies, the encounter shifts from the dead player to the ranger, and the encounter will start attacking after a 1 turn delay." \n 
            '(this class ability can only be used if the Ranger posseses a DEX-Based Ranged weapon).'
        
        if pl8['class'] == 'Monk':
            pl8['class_ability'] = "Taoism: At any point in combat the Monk can make two attacks in one turn, the standard dealing 100% damage and the second strike at half damage value of the first strike." \n
            "This ability isn't usable when the Monk is using a two handed weapon, (Has a cooldown of 3 turns)."
        
        if pl8['class'] == 'Warlock':
            pl8['class_ability'] = "Intertwine Fate: The Warlock can bind a creature of Uncommon or lower ranking to the Warlock." \n 
            'The creature will be decided by drawing monsters from the monster pile until a common or uncommon monster card is drawn.' \n 
            'The creature and Warlock are bound by life, when the creature dies the Warlock receives damage depending on the ranking of the monster (Common = 5 damage, Uncommon = 10 damage).' \n 
            "The creature acts directly after the Warlock's turn. The warlock can summon another creature if their current creature has died, but with every summoned creature's death, the damage penalty for a creature dying will increase by 2."
            
        if pl8['class'] == 'Wizard':
            pl8['spells'].append('Magic Missile')
            pl8['class_ability'] = "Arcane Expertise: The Wizard is capable of learning any spell, with its cooldown being equal to its rarity," \n
            '(magic missile no cooldown, uncommon 2 battles, rare 3 battles, legendary 4 battles, The Wizard cannot learn resurection magic.)'
        
        elif pl8['class'] == 'Saint':
            pl8['spells'].append('Recover')
            pl8['class_ability'] = 'Divine Blessing: When the Saint uses a healing type spell they can make the effects party wide' \n 
            'for as long as the group is fighting within the same encounter, or on the same space.'
        '''
# Limit Breaking #


    
# Stat Handling Functions #

def incr_hp(pl, amount):
    if amount < 1:
        raise "Negative Value: error, please insert a positive integer."
    elif amount == float:
        raise "ValueError: Please insert a positive integer."
    else:    
        pl['hp'] += amount
        if pl['hp'] > pl['max_hp']:
            pl['hp'] = pl['max_hp']
    return
    
def incr_str(pl, amount):
    if amount < 1:
        raise "ValueError: Please insert a positive integer."
    elif amount == float:
        raise "TypeError: Please insert a positive integer."        
    else:  
        if pl['str'] == 5 and pl['limit_break_str'] == True:  
            pl['str'] = 6  
        else: 
            pl['str'] += amount
            if pl['str'] > 5:
                pl['str'] = 5
    return
    
def incr_dex(pl, amount):
    if amount < 1:
        raise "ValueError: Please insert a positive integer."
    elif amount == float:
        raise "TypeError: Please insert a positive integer."
    else:  
        if pl['dex'] == 5 and pl['limit_break_dex'] == True:
            pl['dex'] = 6  
        else: 
            pl['dex'] += amount
            if pl['dex'] > 5:
                pl['dex'] = 5
    return

def incr_agi(pl, amount):
    if amount < 1:
        raise "ValueError: Please insert a positive integer."
    elif amount == float:
        raise "TypeError: Please insert a positive integer."
    else:  
        if pl['agi'] == 5 and pl['limit_break_agi'] == True:
            pl['agi'] = 6  
        else: 
            pl['agi'] += amount
            if pl['agi'] > 5:
                pl['agi'] = 5
    return

def incr_int(pl, anmount):
    if amount < 1:
        raise "ValueError: Please insert a positive integer."
    elif amount == float:
        raise "TypeError: Please insert a positive integer."
    else:  
        if pl['int'] == 5 and pl['limit_break_str'] == True:
            pl['int'] = 6  
        else: 
            pl['int'] += amount
            if pl['int'] > 5:
                pl['int'] = 5
    return

def incr_max_hp(pl, amount):
    if amount < 1:
        raise "ValueError: Please insert a positive integer."
    elif amount == float:
        raise "TypeError: Please insert a positive integer."
    else:  
        pl['max_hp'] += amount
    return
def incr_spells(pl, amount):
    pass


## UI ##

def setup():
    '''Sets up the background color, screensize and fills it with color, along with the general layout.'''
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
    
# Inventory and Update Buttons #
    
    fill(218,165,32)
    rect(1125, 745, 125, 50)
    rect(1275, 745, 125, 50)
    
# Player Tabs #

    fill(218, 165, 32)
    rect(100, 100, 125, 50)
    rect(150, 100, 125, 50)
    rect(200, 100, 125, 50)
    rect(250, 100, 125, 50)
    rect(300, 100, 125, 50)
    rect(350, 100, 125, 50)
    rect(400, 100, 125, 50)
    rect(400, 100, 125, 50)

# Equiped Inventory Window #
    
    
def mousePressed(x):
    global curr_char
    
def load_images(curr_charr):
    '''Function that deals with displaying and managing class card images within the program.'''
    global warriorimg
    global saintimg
    global wizardimg
    global monkimg
    global rangerimg
    global warlockimg
    global paladinimg
    global rogueimg
    if curr_char == paladin:
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
    text('Class: ', 330, 80)
    text('HP: ', 330, 153)
    text('Max HP: ', 330, 203)
    text('Strength: ', 330, 253)
    text('Dexterity: ', 330, 303)
    text('Agility: ', 330, 353)
    text('Intelligence: ', 330, 403)
    text('Status: ', 330, 453)
    text('Damage: ', 330, 503)
    textSize(20)
    text('Class Ability', 670, 577) 
    text('Spells', 275, 535)
    text('Inventory', 1155, 778)
    text('Update', 1315, 778)
    
def draw_mutable_text_players(pl):
    '''Draws all mutable text for players wihtin the program, using 'pl' as it's parameter.'''
    textSize(15)
    text(str(pl['class']), 450, 60)
    text(str(pl['hp']), 470, 100)
    text(str(pl['max_hp']), 470, 153)
    text(str(pl['str']), 470, 203)
    text(str(pl['dex']), 470, 253)
    text(str(pl['agi']), 470, 303)
    text(str(pl['int']), 470, 353)
    text(str(pl['status']), 470, 403) 
    textSize(10)
    text(str(pl['class_ability']), 670, 610)
    textSize(15)
    if len(pl['spells']) > 0:
        for spell_amount in pl['spells']:
            text(str(pl['spells'][0]), 130, 580)
            text(str(pl['spells'][1]), 130, 610)
            text(str(pl['spells'][2]), 130, 640)
            text(str(pl['spells'][3]), 130, 670)
            text(str(pl['spells'][4]), 130, 700)
    
def update():
    pass
    
def inventory():
    pass
    
def draw():
    draw_unmutable_text()
    draw_mutable_text_players(final_chars[curr_char])
    load_images(curr_char)
