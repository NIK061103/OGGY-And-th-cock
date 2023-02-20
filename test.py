import turtle
import random

wn = turtle.Screen()
wn.bgcolor("black")
wn.title("OGGY AND THE COCKROACHES")
wn.setup(800, 800)
# wn.bgpic('/Users/nikhilrajput/Downloads/âPngtreeâline check paper texture abstract_1465960 Small.png')


class Pen(turtle.Turtle):  # creating the square tile
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("blue")
        self.up()
        self.speed(0)


class Oggy(turtle.Turtle):
    def __init__(self, w):
        self.w = w
        turtle.Turtle.__init__(self)
        self.shape('circle')
        self.color('cyan')
        self.penup()
        self.speed(0)

    def move_left(self):
        x = oggy.xcor() - 20
        y = oggy.ycor()

        if (x, y) not in self.w:
            oggy.setx(x)

    def move_right(self):
        x = oggy.xcor() + 20
        y = oggy.ycor()

        if (x, y) not in self.w:
            oggy.setx(x)

    def move_up(self):
        x = oggy.xcor()
        y = oggy.ycor() + 20

        if (x, y) not in self.w:
            oggy.sety(y)

    def move_down(self):
        x = oggy.xcor()
        y = oggy.ycor() - 20

        if (x, y) not in self.w:
            oggy.sety(y)


class Dee(turtle.Turtle):
    def __init__(self, w):
        self.w = w
        turtle.Turtle.__init__(self)
        self.shape('circle')
        self.color('orange')
        self.penup()
        self.speed(1)


class Joey(turtle.Turtle):
    def __init__(self, w):
        self.w = w
        turtle.Turtle.__init__(self)
        self.shape('circle')
        self.color('purple')
        self.penup()
        self.speed(1)


class Marky(turtle.Turtle):
    def __init__(self, w):
        self.w = w
        turtle.Turtle.__init__(self)
        self.shape('circle')
        self.color('green')
        self.penup()
        self.speed(1)


class Point(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape('triangle')
        self.color('yellow')
        self.penup()



level_1 = [
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "XO    XXXX           XXXXXXXXX",
    "X  XX XXXX XXXXXXX X       DXX",
    "X  XX XXXX XXXXXXX XXXXXXX  XX",
    "X      PXX XXX         XXX  XX",
    "X XXXX XXX XXX XXXXXXXXXXX  XX",
    "X    X XXX XXX XXXP XXXXXX  XX",
    "XXXX X XXX X   XXX          XX",
    "X PX X        XXXX  XXXXXX  XX",
    "X  X X  XXXXXXXXXXXXXXXXXXXXXX",
    "X                            X",
    "XX XXX XXXXXXXXXXXXXXXXXXX X X",
    "X                XXXXX  XX X X",
    "X XXXX XXXX XXX JXXXXX  XX  PX",
    "X X  X XXXX XXX         XXX  X",
    "X                       XPX  X",
    "X XXXXXXXX XXXXXXXXXXXXXX    X",
    "X       XX XXX        XXX XX X",
    "XXXXXXX XX XXX XXXXXX    PXX X",
    "XX PXXX XX               XXX X",
    "XX      XXXXX XXXX  XXXX XXX X",
    "XX XXXX XXXXX    X  XXXX XXX X",
    "X           X XX             X",
    "X XXXXXXXXXXX XX XXXXX XXXX XX",
    "X XX     MXXX XX     X    X  X",
    "X XX XXXX X     X XX   XX XX X",
    "X XX XXXX X  XX X  X XXXX XX X",
    "X         XX XX XX X      XX X",
    "XPXXX XXX       XX   XXXX   PX",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"]


pen = Pen()


def walls():
    wall = []
    for i in range(len(level_1)):
        for j in range(len(level_1[i])):
            screen_x = -300 + (j * 20)
            screen_y = 300 - (i * 20)
            if level_1[i][j] == 'X':
                wall.append((screen_x, screen_y))

    return wall


oggy = Oggy(walls())
dee = Dee(walls())
joey = Joey(walls())
marky = Marky(walls())
point = Point()

for i in range(len(level_1)):
    for j in range(len(level_1[i])):
        c = level_1[i][j]

        screen_x = -300 + (j * 20)
        screen_y = 300 - (i * 20)

        if c == "X":
            pen.goto(screen_x, screen_y)
            pen.stamp()

        if c == 'O':
            oggy.goto(screen_x, screen_y)

        if c == 'D':
            dee.goto(screen_x, screen_y)

        if c == 'J':
            joey.goto(screen_x, screen_y)

        if c == 'M':
            marky.goto(screen_x, screen_y)

        if c == 'P':
            point.goto(screen_x, screen_y)
            point.stamp()


def cal(cock, w):
    c_p = cock.pos()
    p_r = (cock.xcor() + 20, cock.ycor())
    p_l = (cock.xcor() - 20, cock.ycor())
    p_u = (cock.xcor(), cock.ycor() + 20)
    p_d = (cock.xcor(), cock.ycor() - 20)
    l=[p_r,p_l,p_u,p_d]
    for i in l:
        if i in w or i == c_p:
            l.remove(i)
    n_p = random.choice(l)

    cock.goto(n_p)


wn.listen()
wn.onkey(oggy.move_left, 'Left')
wn.onkey(oggy.move_right, 'Right')
wn.onkey(oggy.move_up, 'Up')
wn.onkey(oggy.move_down, 'Down')


n = 0

while(n != 10000):
    cal(dee, walls())
    cal(joey, walls())
    cal(marky, walls())
    n += 1

turtle.mainloop()