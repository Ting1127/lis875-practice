from turtle import *

for i in range(5):
    name = textinput('Name', 'Please enter your name')
    write(name, font=('Roboto', 20, 'normal'))
    penup()
    right(90)
    forward(40)
    left(90)
    pendown()

done()