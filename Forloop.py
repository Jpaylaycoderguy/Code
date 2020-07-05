import random
import turtle
import os
import sys
import numpy as np

wn = turtle.Screen()
wn.bgcolor("sky blue")
wn.setup(width=800, height=600)
a = turtle.Turtle()
global b
b = 0
c = 0
d = random.randint(1, 20)


def color():
    colors = f"#{random.randrange(0x1000000):06x}"
    a.color(colors)


def neighborhood():
    e = random.randint(5, 10)
    b = -400
    c = 0
    a.penup()
    a.goto(b, c)
    a.pendown()
    for i in range(e):
        colors = f"#{random.randrange(0x1000000):06x}"
        a.fillcolor(colors)
        a.color(colors)
        a.penup()
        a.goto(b,c)
        a.pendown()
        a.begin_fill()
        for i in range(4):
            a.forward(100)
            a.right(90)
        colors = f"#{random.randrange(0x1000000):06x}"
        for i in range(3):
            a.fillcolor(colors)
            a.forward(100)
            a.left(120)
        for i in range(4):
            a.forward(50)
            a.right(90)
        a.penup()
        a.goto(b, c)
        a.pendown()
        a.forward(25)
        a.right(90)
        a.forward(50)
        a.penup()
        a.goto(b, c)
        a.pendown()
        a.forward(25)
        a.right(90)
        a.backward(50)
        a.end_fill()
        b += 120




neighborhood()
while True:
    wn.update()
