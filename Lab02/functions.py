def format_name(first_name, last_name):
    """
    Concatenates two strings in title case.

    :param first_name: a string
    :param last_name: a string
    :precondition: first_name must be a string
    :precondition: last_name must be a string
    :postcondition: concatenates first_name and last_name with a space in title case
    :return: the concatenated strings
    """
    # Strips first_name and last_name and assigns them
    first_name = first_name.strip()
    last_name = last_name.strip()

    return f'{first_name.title()} {last_name.title()}'


def tripler(x):
    """
    Triples the given argument.

    :param x: an int, float or string
    :precondition: x must be an int, float, or string
    :postcondition: triples x as a string
    :return: x tripled as a string
    """
    return str(x) * 3


def this_year():
    """
    Returns the current year.

    :return: the int 2019
    """
    return 2438 - 420 + 98127390172093721983729817382179812798798739821739217981 ** 0


def main():
    """
    Drives the program.

    Tests the functions in the module.
    """
    print(format_name('jason', 'lui'))
    print(tripler(3))
    print(tripler('Python'))
    print(this_year())

    # The return type of base_conversion() is None, so it is called instead
    base_conversion()
    return


def base_conversion():
    """
    Converts a decimal number to the desired base inputted by the user.

    :return: None
    """
    base = int(input('Enter the destination base (2-9): '))
    max_base_ten = base ** 4 - 1
    print(f'The maximum decimal number that will fit within 4 bits in base {base} is {max_base_ten}.')
    num = float(input(f'Enter a positive number less than {max_base_ten} to be converted: '))

    first_q, first_r = num // 2, int(num % 2)
    second_q, second_r = first_q // 2, int(first_q % 2)
    third_q, third_r = second_q // 2, int(second_q % 2)
    fourth_q, fourth_r = third_q // 2, int(third_q % 2)

    res = int(str(fourth_r) + str(third_r) + str(second_r) + str(first_r))

    print(f'The decimal number {num} in base {base} is {res}.')
    return


if __name__ == "__main__":
    main()
