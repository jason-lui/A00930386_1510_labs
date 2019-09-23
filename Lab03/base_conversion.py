def base_conversion():
    """
    Convert a decimal number to the desired base inputted by the user.

    :postcondition: converts the inputted number to the desired base
    """
    base = int(input('Enter the destination base (2-9): '))
    max_base_ten = base ** 4 - 1
    print(f'The maximum decimal number that will fit within 4 bits in base {base} is {max_base_ten}.')
    num = int(input(f'Enter a positive number less than {max_base_ten} to be converted: '))
    res = ""

    quotient = num
    res = string_remainder(quotient, base) + res
    quotient = quotient // base
    res = string_remainder(quotient, base) + res
    quotient = quotient // base
    res = string_remainder(quotient, base) + res
    quotient = quotient // base
    res = string_remainder(quotient, base) + res

    res = int(res)

    print(f'The decimal number {num} in base {base} is {res}.')
    return

def string_remainder(quotient, base):
    """
    Returns the remainder as a string.

    :param quotient: an integer
    :param base: an integer
    :precondition: quotient must be an integer
    :precondition: base must be an integer
    :postcondition: generates the remainder as a string
    :return: the remainder as a string
    """
    return str(int(quotient) % 2)

base_conversion()
