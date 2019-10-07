import lab05
import random


def main():
    """

    :return:
    """
    character = []

    # Ask user for the length of their username
    name_length = int(input("Enter the length of your username: "))
    name_length = name_length
    name = lab05.generate_name(name_length)

    # Add the username to character
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

    # Add the stat mini-lists to character in the correct order
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
                 'The Bloodthirster'
                 'Phantom Dancer',
                 'Rapidfire Cannon',
                 'Boots of Lucidity',
                 'Boots of Swiftness',
                 'Boots of Alacrity',
                 'Mercury Treads']

    # Choose up to 8 items from the item list at random
    print("Choosing starting items...")
    print("\n")
    character_items = lab05.choose_inventory(item_list, random.randint(0, 8))

    # Add the item list to the character info
    character.append(character_items)
    lab05.print_character(character)
    return


if __name__ == '__main__':
    main()
