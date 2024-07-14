## Kaden Bilyeu
## 2024-07-14
## Midterm; Question 4
## CS 3080-001
## 4.py

## Testing and debugging here, final answers will be handwritten on the exam.

## Write a function where the parameters are the radius and the height. From this value, calculate and
## return the area of a cylinder, print the value outside of that function

## built-in libraries
import math

def q4_cylinder_area(radius:float, height:float) -> float:
    area = 2 * math.pi * radius * height + 2 * math.pi * radius**2

    ## floats get icky with precision, so we'll round to 3 decimal places out of habit
    return round(area, 3)

radius = float(input("Enter the radius of the cylinder: "))
height = float(input("Enter the height of the cylinder: "))

area = q4_cylinder_area(radius, height)

print(f"The area of the cylinder is: {area}")
