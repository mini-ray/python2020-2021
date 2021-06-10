# recursion
import turtle


def square(t,d):
	#t.speed(0)
	t.pendown()
	t.begin_fill()
	for i in  range (0,4):
		t.fd(d)
		t.rt(90)
	t.end_fill()
	t.penup()
    

def main():
	turtle.tracer(0,0)
	twin = turtle.Screen()
	t = turtle.Turtle()
	#twin.clear()
	count = 0
	for x in range (-400,401,25):
		for y in range (-400,401,25):
			t.penup()
			t.goto(x,y)
			thecolor = "#000000"
			#if (count == 5):
				#thecolor = "#0000ff"
				
			if(count >= 220 and count <= 221):
				thecolor = "#ff0000"
				
			if(count >= 253 and count <= 254):
				thecolor = "#ff0000"
				
			if(count >= 207 and count <= 219):
				thecolor = "#b50000"
				
			if(count >= 240 and count <= 252):
				thecolor = "#b50000"
			
			if(count >= 333 and count <= 356):
				thecolor = "#b50000"
			if(count >= 357 and count <= 358):
				thecolor = "#ff0000"
				
			if(count >= 366 and count <= 384):
				thecolor = "#b50000"
			if(count >= 385 and count <= 392):
				thecolor = "#ff0000"
				
			if(count >= 399 and count <= 409):
				thecolor = "#b50000"
			if(count >= 410 and count <= 426):
				thecolor = "#ff0000"
				
			if(count >= 438 and count <= 440):
				thecolor = "#b50000"	
			if(count >= 441 and count <= 459):
				thecolor = "#ff0000"
				
			if(count >= 471 and count <= 473):
				thecolor = "#b50000"
			if(count >= 474 and count <= 492):
				thecolor = "#ff0000"
				
			if(count >= 504 and count <= 506):
				thecolor = "#b50000"
			if(count >= 507 and count <= 525):
				thecolor = "#ff0000"
				
			if(count >= 537 and count <= 539):
				thecolor = "#b50000"
			if(count >= 540 and count <= 558):
				thecolor = "#ff0000"
				
			if(count >= 570 and count <= 572):
				thecolor = "#b50000"
			if(count >= 573 and count <= 591):
				thecolor = "#ff0000"
				
			if(count >= 597 and count <= 601):
				thecolor = "#b50000"	
			if(count >= 603 and count <= 605):
				thecolor = "#b50000"
			if(count >= 606 and count <= 624):
				thecolor = "#ff0000"
				
			if(count >= 630 and count <= 638):
				thecolor = "#b50000"
			if(count >= 639 and count <= 657):
				thecolor = "#ff0000"
				
			if(count >= 663 and count <= 671):
				thecolor = "#b50000"
			if(count >= 672 and count <= 690):
				thecolor = "#ff0000"
				
			#if (count % 10 == 0):
				#thecolor = "#a503fc"
			t.color(thecolor)
			square(t,20)
			count = count + 1
			#time.sleep(0.2)
			print(count)

	turtle.update()
	twin.exitonclick()

if __name__=="__main__":
	main()