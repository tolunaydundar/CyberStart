# Euclidean Distance Formula: d = √(x₂-x₁)²+(y₂-y₁)²

# Function to calculate the Euclidean distance between two points
def euclideanDistance():
    # Empty list to store the points of the coordinates as tuples
    points = []

    # Loop to get the coordinates of the two points
    for i in range(2):
        x = int(input(f"Enter the value of x{i+1} coordinate: "))
        y = int(input(f"Enter the value of y{i+1} coordinate: "))
        points.append((x, y))

    # Calculating the Euclidean distance between the two points
    distance = ((points[1][0] - points[0][0])**2 + (points[1][1] - points[0][1])**2)**0.5
    result_text = f"The Euclidean distance between the points ({points[0][0]}, {points[0][1]}) and ({points[1][0]}, {points[1][1]}) is: {distance}"

    # Returning the result both as a complete response and a float value
    return result_text, distance

# print(euclideanDistance()[0])