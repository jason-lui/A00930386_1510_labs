def base_conversion():
    """
    Converts a decimal number to the desired base inputted by the user.

    :return: None
    """
    base = int(input('Enter the destination base (2-9): '))
    max_base_ten = base ** 4 - 1
    print(f'The maximum decimal number that will fit within 4 bits in base {base} is {max_base_ten}.')
    num = float(input(f'Enter a positive number less than {max_base_ten} to be converted: '))

    (first_q, first_r) = quotient_remainder_division(num, base)
    (second_q, second_r) = quotient_remainder_division(first_q, base)
    (third_q, third_r) = quotient_remainder_division(second_q, base)
    (fourth_q, fourth_r) = quotient_remainder_division(third_q, base)

    res = int(str(fourth_r) + str(third_r) + str(second_r) + str(first_r))

    print(f'The decimal number {num} in base {base} is {res}.')
    return


def quotient_remainder_division(number, divisor):
    quotient = int(number // divisor)
    remainder = int(number % divisor)
    return (quotient, remainder)


base_conversion()
