import turtle

# Function to draw a rectangle (like a garden) using Turtle
def draw_rectangle(length, width):
    t = turtle.Turtle()
    
    # Draw the rectangle with two long and two short sides
    for repeat in range(2):  # Loop two times to draw the rectangle
        t.forward(length)   # Move forward by length
        t.right(90)         # Turn right 90 degrees
        t.forward(width)    # Move forward by width
        t.right(90)         # Turn right 90 degrees
    
    turtle.done()  # Keeps the window open after drawing

# Get the length and width from the user
length = int(input("Enter the garden length: "))
width = int(input("Enter the garden width: "))

# Draw the rectangle
draw_rectangle(length, width)
