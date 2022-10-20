import turtle

t = turtle.Turtle()


def stairs(size, nb):
    for i in range(0, nb):
        t.forward(size)
        t.left(90)
        t.forward(size)
        t.right(90)
    t.forward(size)


def square(size):
    for i in range(0, 4):
        t.forward(size)
        t.left(90)


def squares(initial_size, nb):
    for i in range(0, nb):
        square(initial_size * (i+1))
        t.left(4)


# stairs(40, 4)

# square(100)
squares(10, 20)

turtle.done()
