def calculate_area(shape, *args):
    if shape == "circle" and len(args) == 1:
        radius = args[0]
        return 3.14159 * radius ** 2
    elif shape == "square" and len(args) == 1:
        side = args[0]
        return side ** 2
    else:
        return "Invalid input"

# Calculate area of a circle
circle_area = calculate_area("circle", 5)
print("Area of the circle:", circle_area)

# Calculate area of a square
square_area = calculate_area("square", 4)
print("Area of the square:", square_area)
