from turtle import *



class Frame(dict):
    def __init__(self, name, x, y, w, h):
        self.name = name
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.pen = Turtle()

        # init display
        pen = self.pen
        pen.speed(10)
        pen.hideturtle()
        self.skipto(self.x, self.y)
        pen.goto(self.x + self.w, self.y)
        self.skipto(self.x, self.y)
        pen.goto(self.x, self.y + self.h)
        self.skipto(self.x, self.y)

        step = self.w/60
        years = [14, 15, 16, 17, 18]
        for i in range(5):
            for j in range(12):
                pen.fd(step)
                pen.right(90)
                pen.pu()
                if j == 11:
                    size = 20
                    text = str(years[i])
                    fsize = 12
                else:
                    size = 15
                    text = str(j+1)
                    fsize = 8
                pen.fd(size)
                pen.write(text, align = 'center', font=("Arial", fsize, "normal"))
                pen.bk(size)
                pen.left(90)
                pen.pd()

    def skipto(self, x, y):
        self.pen.penup()
        self.pen.goto(x,y)
        self.pen.pendown()

    def __getitem__(self, key):
        print('<get>', key)
    def __setitem__(self, key, value):
        print('<set> %s: %s' % (key, value))

class Waveform:
    def __init__(self):
        self.width = 1310
        self.height = 700
        self.win = Screen()
        win = self.win
        win.title('Value Investing')
        win.screensize(self.width, self.height)
        win.setup(width = 1.0, height = 1.0) 

        padx = 5
        pady = 20
        startx = -(self.width/2 - padx)
        starty = -(self.height/2 - pady)
        width = self.width - 2 * padx
        height = self.height - 2 * pady

        hoff = 0
        hmove = height/4
        self.finance = Frame('finance', startx, starty + hoff, width, hmove)
        hoff += hmove + pady
        hmove = height/4
        self.volumn = Frame('volumn', startx, starty + hoff, width, hmove)
        hoff += hmove + pady
        hmove = height - hoff
        self.price = Frame('price', startx, starty + hoff, width, hmove)

    def mainloop(self):
        mainloop()
    