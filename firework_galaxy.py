# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 14:58:34 2021

@author: ericd
"""

"""Firework"""

import turtle, math
import time

t = turtle
turtle.colormode(255)
panel = turtle.Screen()   
w = 600
h = 600
panel.setup(width=w, height=h)


panel.bgcolor(0,0,0)

t.pendown()


colors = ['red', 'white', 'blue']
currentColor = None

#i = loop number

for i in range(100):
    if i < 33: 
        currentColor = colors[0]
    if i > 33 and i < 66:
        
        currentColor = colors[1]
    if i > 66:
        currentColor = colors[2]
    
   


    
    t.goto(0,0)
    t.forward(10+(i*5))
    t.right(15+i)
    t.color(currentColor)

t.done()




























