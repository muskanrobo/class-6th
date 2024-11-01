import turtle
from fractions import Fraction

# Function to draw a pizza slice
def draw_slice(fraction, color, label, start_angle):
    turtle.fillcolor(color)
    turtle.begin_fill()
    
    # Draw the pizza slice
    turtle.setheading(start_angle)  # Set the starting angle for the slice
    turtle.forward(100)  # Move forward to create the crust
    turtle.left(90)  # Turn left to create the slice shape
    turtle.circle(100, float(fraction) * 360)  # Draw the arc of the slice
    turtle.goto(0, 0)  # Return to the center
    turtle.end_fill()
    
    # Position the text label
    turtle.penup()
    label_angle = start_angle + (float(fraction) * 180)  # Midpoint of the slice for the label
    turtle.setheading(label_angle)  # Set heading for label position
    turtle.forward(40)  # Move out from the center to place the label
    turtle.write(label, align="center", font=("Arial", 12, "normal"))
    turtle.goto(0, 0)  # Return to the center
    turtle.pendown()

# Set up the turtle
turtle.speed(1)
turtle.penup()
turtle.goto(0, 0)  # Start at the center
turtle.pendown()

# Draw the pizza slices
draw_slice(Fraction(1, 2), "yellow", "1/2", 90)  # Half a pizza
draw_slice(Fraction(1, 4), "orange", "1/4", 270)  # One quarter of a pizza
draw_slice(Fraction(1, 8), "red", "1/8", 0)  # One eighth of a pizza

# Finish drawing
turtle.hideturtle()  # Hide the turtle cursor
turtle.done()
