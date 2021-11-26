import turtle

from turtle import *

screen = turtle.Screen()
screen.setup(600,700)
screen.bgcolor("blue")
screen.tracer()

ball = turtle.Turtle()
ball.color("yellow")
ball.penup()
ball.shape("circle")
ball.goto(0,300)

def bouncing_Ball(fall):
	ball.goto(0,fall)
	ball.goto(0,-300)
	ball.goto(0,300)
	return

for n in range(1,100,5):
	for n in range(1,50):
		bouncing_Ball(n)
		screen.tracer()
		screen.update()
		
