COVERAGE = 400

# Requests user for room dimensions and paint coats
length = float(input('Enter the length of the room in feet: '))
width = float(input('Enter the width of the room in feet: '))
height = float(input('Enter the height of the room in feet: '))
coats = int(input('Enter the number of coats of paint to apply: '))

# Calculates the cans of paint required from the surface area and coverage needed
surface_area = 2 * length * height + 2 * width + height + length * width
coverage_needed = surface_area * coats
cans_of_paint_required = coverage_needed / COVERAGE

# Prints how many cans of paint are required to paint the room
# Partial cans of paint are rounded upwards because we assume one can't buy partial cans
print(f'You need to buy {int(cans_of_paint_required) + 1} cans of paint to finish the room.')
