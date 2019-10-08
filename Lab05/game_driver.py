import lab05
import random


def main():
    """
    Create a character for Dungeons and Dragons.

    User inputs the length of the name to be generated
    Attributes and inventory are rolled.
    :postcondition: character name, attributes, and inventory will be printed
    """
    character = []

    # Ask user for the length of their username
    name_length = int(input("Enter the length of your username: "))
    name = lab05.generate_name(name_length)

    # Add the username to character info
    character.append(name)

    # Inform the user that their stats are being rolled
    print("Rolling for strength, dexterity, constitution, intelligence, wisdom, charisma...")

    # Roll character stats
    str = lab05.roll_die(3, 6)
    dex = lab05.roll_die(3, 6)
    con = lab05.roll_die(3, 6)
    inn = lab05.roll_die(3, 6)
    wis = lab05.roll_die(3, 6)
    cha = lab05.roll_die(3, 6)
    print(f"You rolled: {str}, {dex}, {con}, {inn}, {wis}, {cha}!")
    print("\n")

    # Add the stat mini-lists to character info in the correct order
    character.append(['Strength', str])
    character.append(['Dexterity', dex])
    character.append(['Constitution', con])
    character.append(['Intelligence', inn])
    character.append(['Wisdom', wis])
    character.append(['Charisma', cha])

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
    num_of_items = int(input("How many items would you like?: "))
    print("\n")
    print("----------------------------------------------------")
    print("\n")
    character_items = lab05.choose_inventory(item_list, num_of_items)

    # Add the item list to the character info
    character.append(character_items)
    lab05.print_character(character)
    return


if __name__ == '__main__':
    main()
