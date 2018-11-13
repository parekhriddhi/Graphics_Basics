def setup():
    size(500,500,P3D)
    
def draw():
    background(255);
    translate(250,250);
    fill(mouseX+55,mouseX+3,mouseY,1000);
    rotate(mouseX);
    sphere(60);
