import turtle
import math;
import numpy as np

cursor = turtle.Turtle()

cursor.color("blue")
cursor.speed(0)

def forward(steps):
  cursor.penup()
  cursor.forward(steps)
  cursor.pendown()

def back(steps):
  cursor.penup()
  cursor.back(steps)
  cursor.pendown()

'''
cursor.setheading(90);

def draw_right_triangle(lower_side):
  cursor.forward(lower_side)
  cursor.left(90)
  cursor.forward(lower_side)
  cursor.left(135)
  hypotenuse = (lower_side ** 2 ) * 2
  cursor.forward(math.sqrt(hypotenuse))
  
def square(size):
  for i in range(4):
    cursor.forward(size);
    cursor.left(90)


      
def polygon(numberOfSides, sideLength):
  if numberOfSides < 3:
    print("Error: Number of sides is < 3, 3 minimum required for a polygon")
  else:  
    for i in range(numberOfSides):
        cursor.forward(sideLength);
        cursor.right(360 / numberOfSides)

def spiral(length, angle):
  while length > 1:
    cursor.forward(length);
    cursor.right(angle)
    length = length - 1;
  
draw_right_triangle(100)
forward(90);
draw_equilateral_triangle(50, "up")
draw_equilateral_triangle(50, "down")

back(70)

draw_right_triangle(40)

square(20)

forward(100);

for i in range(3, 11, 1):
  if i % 2 == 0:
    cursor.color("red")
  else:
    cursor.color("green")
  polygon(i, 20)
  forward(20)
  cursor.left(45)
  cursor.penup()
  cursor.forward(20)
  cursor.pendown()

cursor.right(180)
cursor.penup()
cursor.forward(210)
cursor.pendown()

spiral(30, 30);

cursor.penup()
cursor.goto(0, 0)
cursor.pendown()

radius = 0
space = 5
radians = 0
degrees = 360 * 3

for degree in range(degrees):
  radians = math.radians(degree)
  radius = space * radians  
  x = radius * math.cos(radians)
  y = radius * math.sin(radians)
  cursor.goto(x, y)


# r = aθ
# x(θ) = aθ * cos(θ)
# y(θ) = aθ * sin(θ)
'''

def draw_equilateral_triangle(size, direction):
  for i in range(3):
    cursor.forward(size)
    if(direction == "down"):
      cursor.right(120)
    else:
      cursor.left(120)


def drawPolygon(numberOfSides, sideLength):
  if numberOfSides < 3:
    print("Error: Number of sides is < 3, 3 minimum required for a polygon")
  else:  
    for i in range(numberOfSides):
        cursor.forward(sideLength);
        cursor.left(360 / numberOfSides)

def drawSquare(sideLength):
  for i in range(4):
    cursor.forward(sideLength)
    cursor.right(90);
    
def drawRectangle(width, length):
  for i in range(2):
    cursor.forward(width);
    cursor.right(90)
    cursor.forward(length);
    cursor.right(90)

def drawStopSign(sideLength):
  drawPolygon(8, sideLength)
  cursor.penup()
  multiplier = 3/8
  forward_amount = multiplier * sideLength
  cursor.forward(forward_amount)
  cursor.pendown()
  drawRectangle(.2 * sideLength, 2 * sideLength)
  
cursor.speed(0)
cursor.pensize(5)

drawSquare(100);
draw_equilateral_triangle(20, "up")
cursor.setheading(0)
cursor.forward(80)
draw_equilateral_triangle(20, "up")
back(150);

cursor.color("red")

drawSquare(100)
forward(310)

cursor.penup()
cursor.goto(-100, 0)
cursor.pendown()
size = 20
for i in range(10):
  drawStopSign(size)
  cursor.right(10)
  cursor.forward(10)
  size = size - 1

#drawStopSign(20)
#cursor.right(10)
#cursor.forward(10)
#drawStopSign(20)


print("done")
