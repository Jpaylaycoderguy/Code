import random
import turtle
import sys

wn = turtle.Screen()
colors = ("Dark Red",
          "Yellow",
          "Blue",
          "Red",
          "Green",
          "Black",
          "Brown",
          "Teal",
          "Magenta",
          "Hot pink",
          "Silver",
          "Purple",
          "Navy blue",
          "Gray",
          "Orange",
          "Maroon",
          "Aquamarine",
          "Coral",
          "Fuchsia",
          "Wheat",
          "Lime",
          "Crimson",
          "Khaki",
          "Hot pink",
          "Magenta",
          "Plum",
          "Olive",
          "Cyan",
          "Tan",
          "Dark Green",)


def button():
    buttons = turtle.Turtle(visible=False)
    buttons.penup()
    buttons.goto(-300, 200)
    buttons.pendown()
    for i in range(2):
        buttons.forward(80)
        buttons.left(90)
        buttons.forward(30)
        buttons.left(90)
    buttons.penup()
    buttons.goto(-293, 200)
    buttons.write("EXIT", font=("Times new Roman", 22, "bold"))


def clear_screen():
    while turtle.onkeypress(clear_screen, "c"):
        turtle.clearscreen()
        wn.bgcolor('sky blue')
        button()


def btnclick(x, y):
    if -220 > x > -300 and 200 < y < 229:
        sys.exit(0)


turtle.onscreenclick(btnclick, 1)
turtle.onkeypress(clear_screen, "c")

turtle.listen()

wn = turtle.Screen()
wn.bgcolor('sky blue')
button()
y = random.randint(5, 10)
x = random.randint(50, 100)
square_number = 1


def draw_square():
    global square_number
    global side
    s = turtle.Turtle()
    s.color(random.choice(colors))
    for i in range(y):
        a = random.randint(10, 200)
        b = random.randint(10, 200)
        s.penup()
        s.goto(a, b)
        s.pendown()
        square_number += 1
        for i in range(4):
            s.forward(x)
            s.right(90)
            s.color(random.choice(colors))
    print("There were " + str(square_number) + " squares, which means there were a total of " + str(
        square_number * 4) + " sides.")


draw_square()

while True:
    wn.update()
