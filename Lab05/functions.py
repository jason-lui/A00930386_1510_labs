def roll_die(number_of_rolls, number_of_sides):
    """
    Roll a die a number of times and returns the total. !!!

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

    # Check for that inputs are positive integers
    if number_of_rolls <= 0 or number_of_sides <= 0:
        return 0

    res = 0

    for i in range(number_of_rolls):
        res += random.randint(1, number_of_sides)

    return res


def choose_inventory(inventory, selection):
    """
    !!!
    :param inventory: 
    :param selection: 
    :return:
    """
    import random
    if not inventory and selection == 0:
        return []
    if selection < 0:
        print("WARNING: The selection is negative.")
        return []
    if selection > len(inventory):
        print("WARNING: The selection is larger than the size of the inventory.")
        return sorted(inventory)
    if selection == len(inventory):
        return sorted(inventory)

    # Generates a sorted selection of elements from inventory at random
    random_list = random.sample(inventory, selection)
    return sorted(random_list)


def generate_name(syllables):
    """
    !!!
    :param syllables:
    :return:
    """


def generate_vowel():
    """
    !!!
    :return:
    """
    import random
    vowel_unicodes = [97, 101, 105, 111, 117, 121]
    return chr(random.randint(vowel_unicodes))


def generate_consonant():
    """
    !!!
    :return:
    """


def generate_syllable():
    """
    !!!
    :return:
    """