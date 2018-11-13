t1=3
t2=4
ColorT =10
x = random(t1)
y= random(t2)

def setup():
    size(640,640)
    background(0,155,0)
    
def draw():
    global x,y,t1,t2,ColorT
    background(noise(ColorT)*100)
    ColorT=ColorT+0.01
    x=noise(t1)
    y=noise(t2)      #what does noise do
    x=x*640
    y=y*640
    t1=t1+0.01
    t2=t2+0.01
    ellipse(x,y,30,30)
    
