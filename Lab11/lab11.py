import time
import doctest


def timer(func):
    """
    Wrap a function to time its runtime and write it into a file.

    :param func: a function
    :precondition: func must be a function
    :postcondition: the function's runtime will be wrapped
    :return: the wrapped function
    """
    def wrapper(*args, **kwargs):
        start = time.perf_counter()  # Start time
        func(*args, **kwargs)  # Function call
        end = time.perf_counter()  # End time

        with open('results.txt', 'a') as file_obj:  # Append results to results.txt
            file_obj.write(f"{func.__name__}({args[0]}) completed in {(end - start) * 1000:.4f} milliseconds.")
            file_obj.write("\n")
    return wrapper


@timer
def factorial_iterative(n):
    """
    Calculate the factorial of an integer.

    :param n: an integer
    :precondition: n must be a positive integer
    :postcondition: the factorial of n will be calculated
    :return: the factorial n as an integer

    >>> factorial_iterative(1)
    1
    >>> factorial_iterative(4)
    24
    """
    total = 1
    for num in range(1, n + 1):
        total *= num
    return total


@timer
def factorial_recursive(n: int) -> int:
    """
    Calculate the factorial of an integer.

    :param n: an integer
    :precondition: n must be a positive integer
    :postcondition: the factorial of n will be calculated
    :return: the factorial n as an integer

    >>> factorial_recursive(1)
    1
    >>> factorial_recursive(4)
    24
    """
    return factorial_recursive_helper(n)


def factorial_recursive_helper(n: int) -> int:
    """
    Calculate the current result of the factorial_recursive function.

    :param n: an integer
    :precondition: n must be a positive integer
    :postcondition: the current result multiplied by n will be calculated
    :return: the current result multiplied by n

    >>> factorial_recursive_helper(1)
    1
    >>> factorial_recursive_helper(4)
    24
    """
    if n == 1:  # Base case
        return 1
    else:  # Recursive call
        return n * factorial_recursive_helper(n - 1)


def main():
    """
    Drive the program.
    """
    # Clear results.txt if it exists, otherwise generate a new text file
    with open('results.txt', 'w') as file_obj:
        file_obj.write("")

    for num in range(1, 101):
        factorial_iterative(num)

    for num in range(1, 101):
        factorial_recursive(num)


if __name__ == '__main__':
    main()
    doctest.testmod()
