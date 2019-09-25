def base_conversion():
    """
    Convert a decimal number to the desired base.

    :postcondition: converts the inputted number to the desired base
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

    print(f'The decimal number {num} in base {base} is {res}.')
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
    :postcondition: an integer of the place of a number in the specified base
    :return: an integer of the base converted place
    """
    # Strip the dividend to the desired form
    dividend = dividend // (divisor ** (place - 1))
    return int(dividend % divisor)


def main():
    """
    Drive the main function
    """
    base_conversion()


# Call the main function
if __name__ == '__main__':
    main()
