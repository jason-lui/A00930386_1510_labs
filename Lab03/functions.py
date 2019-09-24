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


def create_name(length):
    """
    Generate a name.

    The length of the name will never be longer than 5 characters.
    :param length: an integer
    :precondition: length must be a positive integer
    :postcondition: a name is generated
    :return:
    """
    if length <= 0:
        return None

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

    A random number is given to map_number to generate a letter.
    :postcondition: a random letter is generated
    :return: a letter as a string
    """
    import random
    return map_number(random.randint(1, 26))


def map_number(num):
    """
    Map a number [1, 26] to a letter from the alphabet.

    :param num: an integer
    :precondition: num must be an integer [1, 24]
    :postcondition: maps num to a letter from the alphabet
    :return: a letter from the alphabet as a string
    """
    if num == 1:
        return "a"
    elif num == 2:
        return "b"
    elif num == 3:
        return "c"
    elif num == 4:
        return "d"
    elif num == 5:
        return "e"
    elif num == 6:
        return "f"
    elif num == 7:
        return "g"
    elif num == 8:
        return "h"
    elif num == 9:
        return "i"
    elif num == 10:
        return "j"
    elif num == 11:
        return "k"
    elif num == 12:
        return "l"
    elif num == 13:
        return "m"
    elif num == 14:
        return "n"
    elif num == 15:
        return "o"
    elif num == 16:
        return "p"
    elif num == 17:
        return "q"
    elif num == 18:
        return "r"
    elif num == 19:
        return "s"
    elif num == 20:
        return "t"
    elif num == 21:
        return "u"
    elif num == 22:
        return "v"
    elif num == 23:
        return "w"
    elif num == 24:
        return "x"
    elif num == 25:
        return "y"
    elif num == 26:
        return "z"


if __name__ == "__main__":
    print(roll_die(3, 6))
    print(create_name(5))