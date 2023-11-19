def calculate_slope(x1, y1, x2, y2):
    try:
        slope = (y2 - y1) / (x2 - x1)
        return slope
    except ZeroDivisionError:
        print("Error: The divisor is zero, the two points are on the vertical line.")
        return None

x1, y1 = 77, 240
x2, y2 = 90, 290

result = calculate_slope(x1, y1, x2, y2)
print("Slope:", result)
