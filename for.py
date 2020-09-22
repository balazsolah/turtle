import turtle               # allows us to use the turtles library
wn = turtle.Screen()        # creates a graphics window
alex = turtle.Turtle()      # create a turtle named alex
n=360
sz=1
h=360/n
for i in range(n):
    alex.forward(sz)
    alex.left(h)
