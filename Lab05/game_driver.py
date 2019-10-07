import lab05


def main():
    """

    :return:
    """
    character = []

    # Ask user for the length of their username
    name_length = input("Enter the length of your username: ")
    name = lab05.generate_name(name_length)
    print(f"Your character's name is {name}.")
    print("\n")
    # Add the username to character
    character.append(name)

    # Inform the user that their stats are being rolled
    print("Rolling for strength, dexterity, constitution, intelligence, wisdom, charisma...")

    # Roll character stats
    str = lab05.roll_die(3, 6)
    dex = lab05.roll_die(3, 6)
    con = lab05.roll_die(3, 6)
    int = lab05.roll_die(3, 6)
    wis = lab05.roll_die(3, 6)
    cha = lab05.roll_die(3, 6)
    print(f"You rolled: {str}, {dex}, {con}, {int}, {wis}, {cha}!")

    # Add the stat mini-lists to character in the correct order
    character.append(['Strength', str], ['Dexterity', dex], ['Constitution', con],
                     ['Intelligence', int], ['Wisdom', wis], ['Charisma', cha])


if __name__ == '__main__':
    main()