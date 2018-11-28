#a function that returns true after something is clicked
def onClick():
    held = False
    while held==False:
        if mousePressed:
            held = True
        if held==True:
            if mousePressed == False:
                return True
    

def draw():
    background(180,180,180)
    rect(5,5,50,30)
    if(onClick()):
        fill(0,0,0)
    else:
        fill(255,255,255)
    
