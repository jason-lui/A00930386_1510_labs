import random


def roll_die(number_of_rolls, number_of_sides):
    """
    Roll a die a number of times and returns the total.

    Return 0 if either parameter is not a positive integer.
    :param number_of_rolls: an integer
    :param number_of_sides: an integer
    :precondition: number_of_rolls must be a positive integer
    :precondition: number_of_sides must be a positive integer
    :postcondition: the sum from the die rolls will be totaled
    :return: the total of the die rolls as an integer
    """
    total = 0

    # Check for that inputs are positive integers
    if number_of_rolls <= 0 or number_of_sides <= 0:
        return total

    # Roll the die the specified times and add rolls to total
    for i in range(number_of_rolls):
        total += random.randint(1, number_of_sides)

    return total


def choose_inventory(inventory, selection):
    """
    Generate random items from an inventory.

    Return an empty list if preconditions are not met.
    :param inventory: an integer
    :param selection: an integer
    :precondition: inventory must be a positive integer
    :precondition: selection must be a positive integer
    :postcondition: a list of random items from the inventory will be generated
    :return: a sorted list of random items
    """
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
    Generate a name containing the specified number of syllables.

    Only names of even length are generated.
    :param syllables: an integer
    :precondition: syllables must be a positive integer
    :postcondition: a name with the correct number of syllables will be generated
    :return: the string with the correct number of syllables in title case
    """
    name = ""

    # Generate n // 2 syllables to form a name of length n
    for i in range(syllables // 2):
        name += generate_syllable()
    return name.title()


def generate_vowel():
    """
    Generate a random vowel (y included).

    :postcondition: a single random vowel will be generated
    :return: the vowel as a string
    """
    vowel_unicode = [97, 101, 105, 111, 117, 121]
    return chr(random.choice(vowel_unicode))


def generate_consonant():
    """
    Generate a random consonant.

    :postcondition: a single random consonant will be generated
    :return: the random consonant as a string
    """
    consonant_unicode = [98, 99, 100, 102, 103, 104, 106, 107, 108, 109,
                         110, 112, 113, 114, 115, 116, 118, 119, 120, 121, 122]
    return chr(random.choice(consonant_unicode))


def generate_syllable():
    """
    Generate a syllable containing a random consonant preceding a random vowel.

    :postcondition: a random consonant and a random vowel will be returned
    :return: a string containing a consonant and a vowel
    """
    return generate_consonant() + generate_vowel()


def create_character(name_length):
    """
    Generate a character's name and attributes.

    Attributes are strength, dexterity, constitution, intelligence, wisdom, and charisma.
    Attributes are rolled using 3 6-sided dice.
    :param name_length: an integer
    :precondition: name_length must be an even positive integer
    :postcondition: a character's name, and attributes will be generated
    :return: a list containing a character's name and attributes
    """
    char = []
    name = generate_name(name_length)
    char.append(name)

    str = roll_die(3, 6)
    strength = ['Strength', str]
    char.append(strength)

    dex = roll_die(3, 6)
    dexterity = ['Dexterity', dex]
    char.append(dexterity)

    con = roll_die(3, 6)
    constitution = ['Constitution', con]
    char.append(constitution)

    inn = roll_die(3, 6)
    intelligence = ['Intelligence', inn]
    char.append(intelligence)

    wis = roll_die(3, 6)
    wisdom = ['Wisdom', wis]
    char.append(wisdom)

    cha = roll_die(3, 6)
    charisma = ['Charisma', cha]
    char.append(charisma)

    return char


def print_character(character):
    """

    :param character:
    :return:
    """
    print(f"Your character's name is {character[0]}.")
    print("\n")
    print("--Attributes--")
    print("Strength:", character[1][1])
    print("Dexterity:", character[2][1])
    print("Constitution:", character[3][1])
    print("Intelligence:", character[4][1])
    print("Wisdom:", character[5][1])
    print("Charisma:", character[6][1])

    # Character has an inventory
    if len(character) == 8:
        print("\n")
        print("--Inventory--")
        for item in character[7]:
            print(item)
    return
