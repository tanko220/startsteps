import math

def radians_to_degrees(radians):
    degrees = radians * (180 / math.pi)
    return degrees

# Example usage:
radians = float(input("Enter angle in radians: "))
degrees = radians_to_degrees(radians)
print("Angle in degrees:", degrees)