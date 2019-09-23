# Assigns PI and radius
PI = 3.14159
radius = 0

# Assigns the user input in radius and assigns 2 times the input in double
radius = float(input('Enter a radius for a circle: '))
double = radius * 2

# Calculates the circumference and area using radius and assigns them
circumference = 2 * PI * radius
print(circumference)
area = PI * radius * radius
print(area)

# Calculates the circumference and area using double and assigns them
double_circumference = 2 * PI * double
print(double_circumference)
double_area = PI * double * double
print(double_area)

# Prints the increase in circumference and area when radius doubles
print(f'The circumference increases by {double_circumference / circumference} '
      f'times and the area increases by {double_area / area} times when the radius doubles.')
