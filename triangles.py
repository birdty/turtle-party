import turtle

turtle.width(2)
turtle.speed(0)

def triangle(side_length, direction):
    for i in range(3):
        turtle.forward(side_length)
        if direction == 'down':
            turtle.right(120)
        else:
            turtle.left(120)

def leftTriangle(side_length, direction):
    for i in range(3):
        turtle.back(side_length)
        if direction == 'down':
            turtle.left(120)
        else:
            turtle.right(120)

triangle(100, 'up')
triangle(100, 'down')
leftTriangle(100, 'up')
leftTriangle(100, 'down')

turtle.Screen().exitonclick()


