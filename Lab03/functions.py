def roll_die(number_of_rolls, number_of_sides):
    """
    Roll a die a number of times and returns the total.

    Return 0 if either parameter is not a positive integer. No more than 3 rolls.
    :param number_of_rolls: an integer
    :param number_of_sides: an integer
    :precondition: number_of_rolls must be positive
    :precondition: number_of_sides must be positive
    :postcondition: the sum from the die rolls will be calculated
    :return: the total of the die rolls
    """
    import random
    res = 0
    if number_of_rolls == 0 or number_of_sides == 0:
        return None
    if number_of_rolls >= 1:
        res += random.randint(1, number_of_sides)
    if number_of_rolls >= 2:
        res += random.randint(1, number_of_sides)
    if number_of_rolls >= 3:
        res += random.randint(1, number_of_sides)
    return res


if __name__ == "__main__":
    print(roll_die(3, 6))