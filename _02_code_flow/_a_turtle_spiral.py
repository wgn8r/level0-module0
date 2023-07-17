import random
import turtle
import random


# Returns a random color!
def get_random_color():
    return "#%06X" % (random.randint(0, 0xFFFFFF))


# ====================== DO NOT EDIT THE CODE ABOVE ===========================


if __name__ == '__main__':
    window = turtle.Screen()
    window.bgcolor('white')

    # Make a new turtle
    hi = turtle.Turtle()
    # This code sets our shape to a turtle
    hi.shape("turtle")
    # Set your turtle's speed (0=fastest, 1=slowest, 10=faster)
    hi.speed(10)
    # Set your turtle's color using .color('green')
    hi.color('blue')

    # Use a loop to repeat the code below 50 times
    colors = ["blue", "red", "green", "purple", "pink"]
    for i in range(50):
        hi.color(random.choice(colors))
        hi.forward(3*i)
        hi.right(50)
        hi.turtlesize(stretch_wid=1)

    # Set the turtle color to a random color

    # Move the turtle (5*i) pixels. 'i' is the loop variable

    # Turn the turtle (360/7) degrees to the right

    # Change the turtle width to 'i' (the loop variable)

    # Check the pattern against the picture in the recipe. If it matches, you are done!

    # ===================== DO NOT EDIT THE CODE BELOW ============================
    turtle.done()
