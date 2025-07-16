import turtle 

t = turtle.Turtle()

def draw_pie(n):
    for i in range(n):
        triangle()

def triangle():
    for i in range (3):
        t.forward(80)
        t.left(120)
    t.left(60)

draw_pie(6)
turtle.done()

