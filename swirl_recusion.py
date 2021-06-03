import turtle

def arcR(t,x,y,l,tn,h):
	#x, y, l (length) tn(turn value)
	t.down()
	#t.seth(h)
	for i in range (1,10):
			t.forward(l)
			t.rt(tn)
			
def swirl(t,c,x,y,a,b):
    #print(x,y)
    arcR(t,x,y,a,b,90)
    if c < 105:
        #t.color(r*10,g*5,b*2) #= "#foof";t.color(tcolor)
        arcR(t,x,y,a,b,90)
        a = a / 1.05
        b = b * 1.01
        c = c + 1
        swirl(t,c,x,y,a,b)
    t.circle(c)
    #tcolor = "#800080";t.color(tcolor)
    #arcR(t,x,y,75,11.25,0)
    
def main():
	
	x = 0; y = 400
	w = turtle.Screen()
	w.setup(1500, 1000)
	w.clear()
	w.bgcolor("#ffffff")
	t = turtle.Turtle()
	t.penup()
	t.goto(x,y)
	t.pendown()
	t.speed(0)
	r = 1; g = 1; b = 1
	swirl(t,0,x,y,75,11.25)
	w.exitonclick()
			
if __name__ == '__main__':
	main()
