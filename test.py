sql = 'hello world' \
    '   my name is xue'
print(sql)
quit()

import turtle as tt

def func(x, y):
    print('hello:',  x, y)

tt.goto(0, 200)
tt.onclick(func)
tt.write('hello world',  'left')
tt.home()

tt.mainloop()
while True:
    pass

tt.begin_fill()
tt.speed(3)

# forward | fd ; backward | bk
tt.forward(100)  
# right | rt ;  left | lt;
tt.right(90)    
tt.backward(100)  
# setpos | setposition | goto(x, y= None)
tt.goto(0, 0)  
# setx; sety
tt.setx(-100)  
# seth | setheading; heading.  standard mode, x, left; logo mode, y, right. 
tt.seth(90) 
tt.sety(100)
# home
tt.home()
tt.circle(50, extent = 360)
tt.home()
tt.circle(-50, extent = 270, steps = 2)
tt.seth(270)    
# radius, 半径（+:沿切线向左, -:沿切线向右). extent, 画多少度角， steps, 把弧长分割成多少步
tt.circle(radius = 50, extent = 360, steps = 5) 
print('pensize: ', tt.pensize(), 'heading: ', tt.heading(), 'postition: ', tt.position(), 'speed: ', tt.speed())
tt.penup()
tt.goto(0, 50)
tt.pendown()
tt.dot(10, 'red')

tt2 = tt.Turtle()
tt2.goto(200, 200)
tt.end_fill()


tt.mainloop()