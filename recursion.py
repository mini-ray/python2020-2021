import turtle
import random


def square(t,d):
	#t.speed(0)
	t.pendown()
	
	for i in  range (0,4):
		t.fd(d)
		t.rt(90)
	
	t.penup()
	
def triangle(t,d):
	#t.speed(0)
	t.pendown()
	
	for i in  range (0,3):
		t.fd(d)
		t.rt(120)
	
	t.penup()



def swirl(t):
    x = 0; y = 0
    t.speed(0)
    t.penup()
    r = 0; s = 0
    #t.goto(0,0)
    t.pendown()
    
    for i in range(1,370):
        tcolor = "#0000ff";t.color(tcolor)
        square(t,400)
        tcolor = "#00ff00";t.color(tcolor)
        triangle(t,300)
        t.rt(1)
        t.goto(x,y)
        x = x-r
        y = y-s
        r = random.randint(-1,1)
        s = random.randint(-1,1)
        
    #tcolor = "#800080";t.color(tcolor)
    #arcR(t,x,y,75,11.25,0)


    
			
if __name__ == '__main__':
	x = 0; y = 0
	w = turtle.Screen()
	w.setup(1500, 1000)
	w.clear()
	w.bgcolor("#ffffff")
	t = turtle.Turtle()
	swirl(t)
	w.exitonclick()
