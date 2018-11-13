
x=25.0
y=375.0
speed=5.0
speed1=6.0

def setup():
    size(500,600)
    
def draw():
    global x
    global y
    background(0)
    if (x>=25 and x<=475):
        if  (keyPressed):
            if (keyCode==39):
                move(speed)
            elif (keyCode==37):
                move(0-speed)
    elif x<25:
        x=25
    elif x>475:
        x=475
        
    if (y>=25 and y<=375):
        if (keyPressed):
            
           if (keyCode==38):
               move1(0-speed1)
           elif(keyCode==40):
               move1(speed1)
    elif y<25:
        y=25
    elif y>375:
        y=375
    
    display()
            
        
    
def move(a):
    global x
    x=x+a
    
def move1(a):
    global y
    y=y+a
        
        

def display():
    pushMatrix()
    fill(255)
    ellipse(x,y,50,50)
    popMatrix()
    pushMatrix()
    fill(255,0,0)
    rect(0,400,500,200)
    popMatrix()
