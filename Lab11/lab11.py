import datetime


def timer(func):
    def wrapper(*args, **kwargs):
        start = datetime.datetime.now()
        func(*args, **kwargs)
        end = datetime.datetime.now()
        print(f"Runtime: {start - end}")

        with open('results.txt', 'a') as file_obj:
            file_obj.write(f"{func} completed in {start - end}")
            file_obj.write("\n")
    return wrapper


@timer
def factorial_iterative(n):
    """

    :return:
    """
    total = 1
    for num in range(1, n + 1):
        total *= num
    return total


@timer
def factorial_recursive(n):
    """

    :return:
    """
    total = 1
    if n > 0:
        total *= n
        factorial_recursive_helper(n - 1)

def factorial_recursive_helper(n):
    """

    :return:
    """



def main():
    """

    :return:
    """
    num = 100
    print(factorial_iterative(num))
