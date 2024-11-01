import turtle

# Function to classify the type of triangle based on side lengths
def classify_triangle(a, b, c):
    if a == b == c:
        return "Equilateral Triangle"  # All sides are the same
    elif a == b or b == c or a == c:
        return "Isosceles Triangle"  # Two sides are the same
    else:
        return "Scalene Triangle"  # All sides are different

# Function to draw a larger triangle using Turtle Graphics
def draw_triangle(side_length):
    t = turtle.Turtle()
    t.speed(1)  # Set turtle drawing speed (1 is slow, 10 is fast)
    scale_factor = 3  # Scale factor to increase the size of the triangle
    for _ in range(3):  # Draw a triangle with 3 sides
        t.forward(side_length * scale_factor)
        t.left(120)
    turtle.done()

# Input each side length separately
side1 = int(input("Enter the length of side 1: "))
side2 = int(input("Enter the length of side 2: "))
side3 = int(input("Enter the length of side 3: "))

print("Triangle Type:", classify_triangle(side1, side2, side3))

# Draw an equilateral triangle with the scaled size
draw_triangle(side1)
