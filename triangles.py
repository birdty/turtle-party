import turtle

turtle.width(2)
turtle.speed(0)
turtle.color("blue")

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

def upsideDownTriangle(side_length,direction):
    if direction == 'down':
        turtle.right(60)
    else:
        turtle.left(60)
    turtle.forward(side_length)

    for i in range(2):
        if direction == 'down':
            turtle.right(120)
        else:
            turtle.left(120)
        turtle.forward(side_length)

    if direction == 'down':
        turtle.right(60)
    else:
        turtle.left(60)



triangle(100, 'up')
triangle(100, 'down')
leftTriangle(100, 'up')
leftTriangle(100, 'down')
upsideDownTriangle(100, 'down')
upsideDownTriangle(100, 'up')





turtle.Screen().exitonclick()


