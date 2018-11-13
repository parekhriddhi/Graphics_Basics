def setup():
    
    size(500,500);
    background(255,255,120);
    
def draw():
    noFill();
    strokeWeight(random(3,10));
    stroke(random(0,255),random(0,255),random(0,255));
    rainbow_size=random(600,750);
    ellipse(500,500,rainbow_size,rainbow_size);
