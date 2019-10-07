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
    name = ""
    for i in range(syllables):
        name += generate_syllable()
    return name


def generate_vowel():
    """
    !!!
    :return:
    """
    import random
    vowel_unicode = [97, 101, 105, 111, 117, 121]
    return chr(random.choice(vowel_unicode))


def generate_consonant():
    """
    !!!
    :return:
    """
    import random
    consonant_unicode = [98, 99, 100, 102, 103, 104, 106, 107, 108, 109,
                         110, 112, 113, 114, 115, 116, 118, 119, 120, 122]
    return chr(random.choice(consonant_unicode))


def generate_syllable():
    """
    !!!
    :return:
    """
    return generate_consonant() + generate_vowel()


def create_character(name_length):
    """
    !!!
    :param name_length:
    :return:
    """
    char = []
    name = generate_name(name_length // 2)
    char.append(name)

    strength = ['Strength', roll_die(3, 6)]
    char.append(strength)
    dexterity = ['Dexterity', roll_die(3, 6)]
    char.append(dexterity)
    constitution = ['Constitution', roll_die(3, 6)]
    char.append(constitution)
    intelligence = ['Intelligence', roll_die(3, 6)]
    char.append(intelligence)
    wisdom = ['Wisdom', roll_die(3, 6)]
    char.append(wisdom)
    charisma = ['Charisma', roll_die(3, 6)]
    char.append(charisma)

    return char


def print_character(character):
    """

    :param character:
    :return:
    """
    print("Character:", character[0])
    print("\n")
    print("Strength:", character[1][1])
    print("Dexterity:", character[2][1])
    print("Constitution:", character[3][1])
    print("Intelligence:", character[4][1])
    print("Wisdom:", character[5][1])
    print("Charisma:", character[6][1])
