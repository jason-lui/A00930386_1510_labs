import doctest


def base_conversion():
    """
    Convert a decimal number to the desired base.

    :precondition: user must input integers only
    :postcondition: convert the inputted number to the desired base
    """
    base = int(input('Enter the destination base (2-9): '))
    max_base_ten = base ** 4 - 1
    print(f'The maximum decimal number that will fit within 4 bits in base {base} is {max_base_ten}.')
    num = int(input(f'Enter a positive number less than {max_base_ten} to be converted: '))
    res = ""

    res = str(int_div_modulo(1, num, base)) + res
    res = str(int_div_modulo(2, num, base)) + res
    res = str(int_div_modulo(3, num, base)) + res
    res = str(int_div_modulo(4, num, base)) + res

    res = int(res)

    # Print and pad 0's
    print(f'The decimal number {num} in base {base} is {((4 - len(str(res))) * "0") + str(res)}.')
    return


def int_div_modulo(place, dividend, divisor):
    """
    Calculate the remainder for base conversion in places left of the radix point.

    :param place: an integer
    :param dividend: an integer
    :param divisor: an integer
    :precondition: place must be an integer
    :precondition: dividend must be an integer
    :precondition: divisor must be an integer
    :postcondition: an integer of the decimal place as a string
    :return: an string of the base converted place

    >>> int_div_modulo(1, 8, 2)
    0
    >>> int_div_modulo(2, 40, 3)
    1
    """
    # Strip the dividend to the desired form
    dividend = dividend // (divisor ** (place - 1))
    return int(dividend % divisor)


def main():
    """
    Drive the program.
    """
    base_conversion()


if __name__ == '__main__':
    doctest.testmod()
