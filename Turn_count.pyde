# weet niet of het werkt, maar dit had ik bedacht
turn_count = 0
global_turn_count = 0
players = #number of players

def turn_counter():
    if turn_count % players == 0:
        return global_turn_count += 1
