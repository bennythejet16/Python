'''
plt-circle-list-cwc.py
Test this.
https://tritech-testsite.smapply.io/
Use your personal email.  Not your @ksd.org account.

python-circle-list-assignment.py
Get the code: 10.183.1.26 code python
Plot circle data using python
- Use your data
- Change the background color X
- Change the graph line colors
- Change the plot line color X
- Change the plot dot color X
- Label the graph with the text "Plotting Circumference and Diameter" X
- Label the axis with text (Circumference and Diameter) X
- Upload to github with your name initials or name attached (plot-circle-list-cwc.py)

'''

import turtle
import math
wdth = 800; hgth = 800; bgstring = "#008080"
red = "#000000"; green = "#000000"; blue = "#000000"

def grid(t):
	x = 0; y = 0
	while (x < 400):
		t.penup()
		t.goto(x,y)
		t.pendown()
		t.goto(x,y+400)
		x = x + 50
	x = 0; y = 0
	while (y < 400):
		t.penup()
		t.goto(x,y)
		t.pendown()
		t.goto(x+400,y)
		y = y + 50
	t.penup();t.goto(-200,450);t.pendown()
	t.color('#FF050F')
	style = ('Courier', 30, 'bold')
	t.write('Circle Circumference and Diameter Plot', font=("Arial", 18, 'normal', 'bold',))
	t.color('#cc0000')
	t.penup();t.goto(-20,20);t.pendown()
	t.write('C\ni\nr\nc\nu\nm\nf\ne\nr\ne\nn\nc\ne', font=("Arial", 18, 'normal', 'bold',))
	t.color('#cc00cc')
	t.penup();t.goto(80,-50);t.pendown()
	t.write('Diameter', font=("Arial", 30, 'normal', 'bold',))
	t.hideturtle()
	t.penup()

def plotCircles(t):
	#list  named d and c
	t.color('#000000')
	d =  [35,34,12.8, 1.8, 19.8, 8.7] 
	c =  [111,108,37,  4.7, 57.1, 26.1] 
	# list dsorted and csorted
	dsorted = sorted (d, key = float)
	csorted = sorted(c , key = float)
	t.color('#00FF4B')
	t.goto(0,0)
	t.pendown()
	t.dot(3, blue)
	t.goto(dsorted[0],csorted[0])
	t.dot(3, blue)
	t.goto(dsorted[1],csorted[1])
	t.dot(3, blue)
	t.goto(dsorted[2],csorted[2])
	t.dot(3, blue)
	t.goto(dsorted[3],csorted[3])
	t.dot(3, blue)
	t.goto(dsorted[4],csorted[4])
	t.dot(3, blue)
	t.goto(dsorted[5],csorted[5])
	t.dot(3, blue)
	
def main():
	try:
		turtle.tracer(0,0)
		turtle.TurtleScreen._RUNNING = True
		# get wdth and hgth globally
		turtle.screensize(canvwidth=wdth, canvheight=hgth, bg=bgstring)
		print(turtle.Screen().screensize())
		w = turtle.Screen()
		t = turtle.Turtle()
		t.hideturtle()
		grid(t)
		plotCircles(t)
		turtle.update()
		w.exitonclick()
	finally:
		turtle.Terminator()
	
if __name__ == '__main__':
	main()

'''
	# Using sorted + key 
	Output = sorted(Input, key = float) 
	# Using sorted + key 
	Output = sorted(Input, key = float) 
'''
