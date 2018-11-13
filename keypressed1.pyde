def setup():
    size(800,800);
    background(0);

def draw():
    fill(0);
    rect(0,0,width,height);
    
def keyPressed():
    fill(0,240,0);
    textSize(random(20,200));
    text(key,random(300),random(100,400));
