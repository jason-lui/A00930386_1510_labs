import doctest


def time_calculator(seconds):
    """
    Convert the number of seconds into days, hours, minutes, seconds.

    :param seconds: an integer
    :precondition: seconds must be a positive integer
    :postcondition: the days, hours, minutes, seconds will be printed

    >>> time_calculator(0)
    0 0 0 0
    >>> time_calculator(60)
    0 0 1 0
    >>> time_calculator(3600)
    0 1 0 0
    >>> time_calculator(86400)
    1 0 0 0
    >>> time_calculator(100000)
    1 3 46 40
    """
    # Separate desired time frames into variables
    days = time_converter(seconds, "days")
    hours = time_converter(seconds, "hours")
    minutes = time_converter(seconds, "minutes")
    seconds = time_converter(seconds, "seconds")

    print(days, hours, minutes, seconds)
    return


def time_converter(dividend, divisor):
    """
    Return the remainder for a denomination of time.

    Only allows days, hours, minutes and seconds.
    :param dividend: an integer
    :param divisor: an integer
    :precondition: divisor must be an integer
    :postcondition: calculate the remainder
    :return: the converted amount of time

    >>> time_converter(3000, "hours")
    0
    >>> time_converter(4000, "hours")
    1
    >>> time_converter(38000, "hours")
    10
    """
    # Variables of different time frames in seconds
    seconds_per_day = 86400
    seconds_per_hour = 3600
    seconds_per_minute = 60
    second = 1

    if divisor == "days":
        dividend //= seconds_per_day
    if divisor == "hours":
        dividend %= seconds_per_day
        dividend //= seconds_per_hour
    if divisor == "minutes":
        dividend %= seconds_per_hour
        dividend //= seconds_per_minute
    if divisor == "seconds":
        dividend %= seconds_per_minute

    return dividend




def main():
    """
    Drive the program.
    """
    doctest.testmod()


if __name__ == "__main__":
    main()


"""
Component(s) of computational thinking

Decomposition
time_calculator() uses the helper function integer_division() to calculate the
number of days/hours/minutes given a number of seconds. The helper function
can be implemented into any program that requires a conversion of time if given seconds.
"""