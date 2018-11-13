def setup():
    size(800,800)
    background(255)
    noStroke()
    
def draw():
    fill(255,153,51);
    beginShape();
    vertex(50, 50);
    vertex(150,50);
    vertex(170,80);
    vertex(270,80);
    vertex(290,110);
    vertex(390,110);
    vertex(390,160);
    vertex(290,160);
    vertex(270,130);
    vertex(170,130);
    vertex(150,100);
    vertex(50,100);
    endShape(CLOSE);
    pushMatrix()
    fill(0,153,0);
    beginShape();
    vertex(50, 150);
    vertex(150,150);
    vertex(170,180);
    vertex(270,180);
    vertex(290,210);
    vertex(390,210);
    vertex(390,260);
    vertex(290,260);
    vertex(270,230);
    vertex(170,230);
    vertex(150,200);
    vertex(50,200);
    endShape(CLOSE);
    popMatrix()
    pushMatrix()
    noFill()
    ellipse(220,155,50,50)
    stroke(0,0,128)
    popMatrix()
    

    
    
