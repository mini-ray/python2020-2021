import turtle

def arcR(t,x,y,l,tn,h):
	#x, y, l (length) tn(turn value)
	t.down()
	#t.seth(h)
	for i in range (1,10):
			t.forward(l)
			t.rt(tn)
			
def swirl(t):
    x = -400; y = 0
    t.speed(0)
    t.penup()
    a = 75
    b = 11.25
    t.goto(0,400)
    t.pendown()
    
    for i in range(1,110):
        tcolor = "#800080";t.color(tcolor)
        arcR(t,x,y,a,b,90)
        a = a / 1.05
        b = b * 1.01
    #tcolor = "#800080";t.color(tcolor)
    #arcR(t,x,y,75,11.25,0)


    
			
if __name__ == '__main__':
	#x = -400; y = 0
	w = turtle.Screen()
	w.setup(1500, 1000)
	w.clear()
	w.bgcolor("#ffffff")
	t = turtle.Turtle()
	swirl(t)
	w.exitonclick()
