# Turtle party project by Tyler Bird
# This program draws alot of various shapes
# for fun.
# 10/20/2023

import turtle
turtle.width(2)
turtle.speed(0)

def drawSquare(color, length):
    turtle.color(color)
    for i in range(4):
        turtle.forward(length)
        turtle.right(90)

def drawRectangle(width, height, color):
    turtle.color(color)
    for i in range(2):
        turtle.forward(width)
        turtle.right(90)
        turtle.forward(height)
        turtle.right(90)

def moveForward(distance):
    turtle.penup();
    turtle.forward(distance)
    turtle.pendown()

def moveBackward(distance):
    turtle.penup();
    turtle.forward(-distance)
    turtle.pendown()

def drawPolygon(l, n):
    for i in range(n):
        turtle.forward(l)
        turtle.left(360 / n)

drawSquare("red", 50)

moveForward(100)
drawSquare("blue", 50)

moveForward(100)
drawRectangle(50, 80, "blue")

moveBackward(300)
drawRectangle(50, 80, "red")

moveBackward(100)
drawPolygon(50, 3);
drawSquare("green", 50)

moveBackward(100)
drawPolygon(50, 3);
drawSquare("green", 50)

turtle.Screen().exitonclick()
