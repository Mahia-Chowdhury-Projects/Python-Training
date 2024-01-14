"""
Lab 7, Task 4

Implements a module which draws a tree pattern using the Python turtle.
"""

from turtle import *
from sys import argv

def initialize_turtle():
    """Setups up the window and initializes the turtle to be at the base of the
    main trunk facing north. DO NOT MODIFY."""

    # Create a turtle window
    setup(600, 600)
    reset()

    # Configure our turtles line width and speed
    pensize(1) 
    speed(0)   # 0=fastest, 1=slowest, 6=normal

    # By default turtle starts at (0,0), the center of the screen and faces east.
    # We move it to a reasonable spot for a shrub and point it north.
    up()
    goto(-100, -200)
    left(90)
    down()


def draw_shrub(trunk_length, angle, shrink_factor, min_length):
    """
    Draws a shrub as specified in Lab 7 Task 4.
    Returns the total length (float) of branches (including the trunk).
    Assume that the turtle is positioned at the base of the main
    trunk facing north before this function is called.
    """
    if trunk_length < min_length:
        return 0 
    else: 
        fd(trunk_length)
        rt(angle)
        #recursively draw all branches onthe right
        num1 = draw_shrub(trunk_length*shrink_factor, angle, shrink_factor, min_length)
        lt(angle*2)
        #recursively draw all branches on the left
        num2=  draw_shrub(trunk_length*shrink_factor*shrink_factor, angle, shrink_factor, min_length)
        rt(angle);bk(trunk_length)

    return trunk_length + num1+num2
          

# When run as a script, take a picture size and the gap between
# concentric squares as command-line arguments.
if __name__=='__main__':
    """Testing code. DO NOT MODIFY."""
    if len(argv) != 5:
        print("Provide a trunk length, angle, shrink factor, and min length, eg:\n")
        print("  python3 shrub.py 100 15 0.5 60\n")
    else:
        trunk_length = float(argv[1])
        angle = float(argv[2])
        shrink_factor = float(argv[3])
        min_length = float(argv[4])

        initialize_turtle()
        num_branches = draw_shrub(trunk_length, angle, shrink_factor, min_length)
        print('draw_shrub({}, {}, {}, {}) -> {}'.format(trunk_length, angle, shrink_factor,
                                min_length, num_branches))
        getscreen().getcanvas().postscript(file="shrub-{}-{}-{}-{}.ps".format
                                (trunk_length, angle, shrink_factor, min_length))

        # Comment out the line below if you want
        # the turtle screen to close automatically.
        exitonclick()
