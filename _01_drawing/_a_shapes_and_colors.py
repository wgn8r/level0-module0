import turtle

if __name__ == '__main__':
    window = turtle.Screen()
    window.bgcolor('white')

    # This code makes a new Turtle. Pick a new name for the turtle
    Hello_World= turtle.Turtle()

    # Make your turtle's shape 'turtle', .shape('turtle')
    Hello_World.shape('turtle')

    # Set your turtle's speed using .speed(2)
    Hello_World.speed(2)

    # Set your turtle's color using .color('green') and .pencolor('blue')
    Hello_World.color('green')
    Hello_World.pencolor('blue')
    # Move your turtle forward using .forward(100)
    # TEST    Did your turtle move forward?
    Hello_World.forward(100)
    # Move your turtle left or right using .left(90) or .right(90)
    #for i in range(3):
        #Hello_World.left(90)
        #Hello_World.forward(100)
    # Now put the forward and left/right code into a for loop to repeat 4 times.
    # TEST    Did your turtle draw a square?

    # Move your turtle to a new place on the screen using .goto(x, y)
    # x=0 and y=0 is the center of the screen
    #Hello_World.goto(53,21)
    # Have your turtle draw a circle using .circle(radius, steps=30)
    # TEST    Did your turtle draw a circle?
    Hello_World.color("red")
    Hello_World.begin_fill()
    Hello_World.circle(25,steps=30)
    Hello_World.end_fill()
    Hello_World.color("green")
    Hello_World.circle(25, steps=30)
    # Add color to your shape by adding .begin_fill() before drawing the circle
    # and .end_fill() below

    # Draw 3 more shapes with different fill colors!
    Hello_World.color("red")
    Hello_World.begin_fill()
    Hello_World.circle(25, steps=30)
    Hello_World.end_fill()

    Hello_World.color("blue")
    Hello_World.begin_fill()
    for i in range(3):
        Hello_World.left(90)
        Hello_World.forward(100)
    Hello_World.end_fill()
    Hello_World.color("green")
    Hello_World.begin_fill()
    for i in range(5):
        Hello_World.left(150)
        Hello_World.forward(50)
    Hello_World.end_fill()
    # ===================== DO NOT EDIT THE CODE BELOW ============================
    turtle.done()
