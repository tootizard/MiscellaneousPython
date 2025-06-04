#!/bin/python3

from turtle import *

def do_not_close():
	while(True):
		pass

def rgb_stack():
	width(10)
	for i in range(10):
		for c in ('red','green', 'blue'):
			color(c)
			forward(100)
		up()
		goto(0,ycor()+10)
		down()

def rgb_spiral():
	width(10)
	for i in range(50):
		for c in ('red','green', 'blue','pink','orange'):
			color(c)
			forward(i)
			left(15)

def sun_corporation():
	speed(0)
	right(30)
	length = 50
	for c in ('red','orange','pink','green','teal'):
		fillcolor(c)
		color(c)
		begin_fill()
		for i in range(4):
			forward(length)
			right(90)
		end_fill()
		up()
		goto(xcor()+length,0)
		down()
	up()
	goto(0-length/2,0-(2*length)-20)
	down()
	color('orange')
	write('Sun Corporation', font=('Verdana',30,'normal'))

def multi_turt():
	turts = []
	for i in range(50):
		turts.append(Turtle())
	for turt in turts:
		index = turts.index(turt)
		turt.speed(10)
		turt.up()
		turt.goto(0,index*5)
		turt.down()
		turt.forward(index)

#rgb_stack()
#rgb_spiral()
#sun_corporation()
multi_turt()
do_not_close()
