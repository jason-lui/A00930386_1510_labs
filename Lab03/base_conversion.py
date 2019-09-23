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