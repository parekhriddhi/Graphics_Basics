
def setup():
    global X;
    global Y;
    size(500,500);
    noStroke();
    background(0);
    X=random(0,500);
    Y=random(0,500);

def draw():
    global X;
    global Y;
    fill(0,50);
    rect(0,0,width,height);
    fill(255);
    ellipse(random(width),random(height),10,10);

    
