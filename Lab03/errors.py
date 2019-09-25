def main():
    """
    Drive the main function.
    """
    # ZeroDivisionError
    integer = 10
    zero_error_1 = integer / 0
    zero_error_2 = integer % 0

    # IndexError
    string = "abc"
    index_error_1 = string[10]
    index_error_2 = string[-10]

    # TypeError
    letter = "a"
    type_error_1 = string + integer
    type_error_2 = integer[-10]


# Call the main function
if __name__ == '__main__':
    main()


# Call the main function
if __name__ == '__main__':
    main()