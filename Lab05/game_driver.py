import lab05


def main():
    """
    Create a character for Dungeons and Dragons.

    User inputs the length of the name to be generated
    Attributes and inventory are rolled.
    :postcondition: character name, attributes, and inventory will be printed
    """

    # Ask user for the length of their username
    name_length = lab05.roll_die(1, 6)
    print(f"You rolled {name_length}! your name will be {name_length * 2} characters long.\n")

    # create_character() calls roll_die() and create_name()
    # create_name() calls generate_syllable()
    # generate_syllable() calls generate_consonant() and generate_vowel()
    # Inform the user that their stats are being rolled
    print("Rolling for strength, dexterity, constitution, intelligence, wisdom, charisma...")
    character = lab05.create_character(name_length)

    # Show rolls
    print(f"You rolled: {character[1][1]}, {character[2][1]}, {character[3][1]}, {character[4][1]}, {character[5][1]}, {character[6][1]}!")
    print("\n")

    # A list of possible items in the game
    item_list = ['Rabadon\'s Deathcap',
                 'Seraph\'s Embrace',
                 'Liandry\'s Torment',
                 'Morellonomicon',
                 'Warmog\'s Armor',
                 'Randuin\'s Omen',
                 'Banshee\'s Veil',
                 'Abyssal\' Mask',
                 'Infinity Edge',
                 'The Bloodthirster',
                 'Phantom Dancer',
                 'Rapidfire Cannon',
                 'Boots of Lucidity',
                 'Boots of Swiftness',
                 'Boots of Alacrity',
                 'Mercury Treads']

    # Show items in the store
    print("--Available items in the store--")
    for item in item_list:
        print(item)
    print("\n")

    # Ask user for how many items they would like
    num_of_items = int(input("How many items would you like? (MAX 16): "))
    print("\n")
    print("----------------------------------------------------")

    # Choose items for the character's inventory using choose_inventory()
    character_items = lab05.choose_inventory(item_list, num_of_items)
    character.append(character_items)

    # Print character info using print_character()
    lab05.print_character(character)
    return


if __name__ == '__main__':
    main()
