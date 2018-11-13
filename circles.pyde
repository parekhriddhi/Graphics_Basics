def setup():
    size(255,255)

def draw():
    translate(mouseX,mouseY);
    fill(mouseX,mouseY+2,mouseX+mouseY,1020);
    ellipse(0,0,50,50);
    
