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


def create_name(length):
    """
    Generate a name.

    The length of the name will never be longer than 5 characters.
    :param length: an integer
    :precondition: length must be a positive integer
    :postcondition: a name is generated
    :return: a name as a string in title case
    """
    if length <= 0:
        return
    res = ""

    if length >= 1:
        res += generate_letter()
    if length >= 2:
        res += generate_letter()
    if length >= 3:
        res += generate_letter()
    if length >= 4:
        res += generate_letter()
    if length >= 5:
        res += generate_letter()

    return res.title()


def generate_letter():
    """
    Generate a letter.

    A random number [97, 122] is given to chr() to generate a letter.
    :postcondition: a random letter is generated
    :return: a letter as a string
    """
    import random
    return chr(random.randint(97, 122))


if __name__ == "__main__":
    print(roll_die(3, 6))
    print(create_name(5))
