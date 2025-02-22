def line_equation_from_coordinates(x1, y1, x2, y2):
    """
    Calculates the equation of a line in the form y = mx + b,
    given two coordinate points (x1, y1) and (x2, y2).

    Args:
        x1 (float): x-coordinate of the first point.
        y1 (float): y-coordinate of the first point.
        x2 (float): x-coordinate of the second point.
        y2 (float): y-coordinate of the second point.

    Returns:
        str: A string representing the equation of the line in the form "y = mx + b".
             Returns an appropriate message if the line is vertical or if the points are the same.
    """

    if x1 == x2:
        if y1 == y2:
            return "The two points are the same, cannot define a unique line."
        else:
            return f"x = {x1} (Vertical line)"  # Vertical line equation

    # Calculate the slope (m)
    m = (y2 - y1) / (x2 - x1)

    # Calculate the y-intercept (b) using the point-slope form: y - y1 = m(x - x1)  =>  b = y1 - mx1
    b = y1 - m * x1

    return f"y = {m:.2f}x + {b:.2f}"  # Format the equation string


# Example Usage:
x1 = 1
y1 = 2
x2 = 3
y2 = 6

equation = line_equation_from_coordinates(x1, y1, x2, y2)
print(equation)  # Output: y = 2.00x + 0.00

# Example with a vertical line:
x1 = 5
y1 = 1
x2 = 5
y2 = 4
equation = line_equation_from_coordinates(x1, y1, x2, y2)
print(equation)  # Output: x = 5 (Vertical line)

# Example with same points:
x1 = 2
y1 = 3
x2 = 2
y2 = 3

equation = line_equation_from_coordinates(x1, y1, x2, y2)
print(equation)  # Output: The two points are the same, cannot define a unique line.
