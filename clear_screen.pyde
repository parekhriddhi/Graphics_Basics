def setup():
    size(255,255);
    
def click():
    if(mousePressed):
        background(255);
 
def draw():
    translate(mouseX,mouseY);
    fill(mouseX,mouseY+2,mouseX+mouseY,1020);
    click();
    ellipse(0,0,50,50);
    

    
