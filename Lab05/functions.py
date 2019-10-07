def roll_die(number_of_rolls, number_of_sides):
    """
    Roll a die a number of times and returns the total.

    Return 0 if either parameter is not a positive integer.
    The die is rolled no more than 3 times.
    :param number_of_rolls: an integer
    :param number_of_sides: an integer
    :precondition: number_of_rolls must be positive
    :precondition: number_of_sides must be positive
    :postcondition: the sum from the die rolls will be calculated
    :return: the total of the die rolls

    # Do not know how to doctest random functions at the moment
    """
    import random
    res = 0

    if number_of_rolls == 0 or number_of_sides == 0:
        return
    if number_of_rolls >= 1:
        res += random.randint(1, number_of_sides)
    if number_of_rolls >= 2:
        res += random.randint(1, number_of_sides)
    if number_of_rolls >= 3:
        res += random.randint(1, number_of_sides)

    return res