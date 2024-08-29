import math
def sphere_volume(radius):
    """Calculate the volume of a sphere given its radius."""
    return (4 / 3) * math.pi * (radius ** 3)
radius = 5
volume = sphere_volume(radius)
print(f"The volume of a sphere with radius {radius} is: {volume:.2f}")
