# bouncing simulator

import turtle

window = turtle.Screen()
window.bgcolor("white")
window.title("bouncing simulator :D")

ball01 = turtle.Turtle()
ball01.shape("triangle") #it can be any shape you want :)
ball01.penup()
ball01.speed(0)
ball01.goto(0, 200)
ball01.dy = -2

gravity = 0.08

while True:
    ball01.dy -= gravity
    ball01.sety(ball01.ycor() + ball01.dy)

    if ball01.ycor() < -300:
        ball01.dy *= -1


window.mainloop()

#end notes
#this was a lot of fun to make
#you can use this code and change coordinates/speed/shape/color to get desired animation!
#you can also add more shapes to bounce but this is just an example with one:)
#made May 12th, 2020 
#did this instead of studying for my AP comp sci exam I have in a few days which isn't even in this language LOL
