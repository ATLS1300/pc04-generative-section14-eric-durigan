# -*- coding: utf-8 -*-
"""
Created on Thu Sep 23 13:26:45 2021

@author: ericd
"""
import turtle

def show_pos(x,y):
    print(x,y)

  
screen = turtle.Screen()   
w = 600
h = 600
screen.setup(width=w, height=h)
pen = turtle.Turtle()
pen2 = turtle.Turtle()

screen.listen()
screen.onclick(show_pos)

turtle.colormode(255)

#I want to stamp a square
for i in range(20): 
   pen.pencolor("midnightblue")
   pen.fillcolor("cornflower blue")
   pen.shape("square")
   pen.stamp()
   pen.forward(100)
   pen.right(50)
pen.penup()

for i in range(20): 
   pen2.pencolor("midnightblue")
   pen2.fillcolor("gold")
   pen2.shape("square")
   pen2.stamp()
   pen2.forward(100)
   pen2.right(50)
pen2.penup()


pen.pendown()
pen.shape("square")
pen.pencolor("midnight blue")
pen.fillcolor("cornflower blue")

pen.shapesize(500 / 20)
pen.stamp()

# I want to stamp a circle
pen.shape("circle")

pen.stamp()
for i in range(100): 
   pen.pencolor("gold")
   pen.fillcolor("gold")
   pen.circle(10)
   pen.forward(50)
   pen.right(30)

turtle.done()












#Squaring a circle