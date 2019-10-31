import random


def list_tagger(batch):
    """
    Tag a list with its length.

    :param batch: a list
    :precondition: batch must be a list
    :postcondition: the length of the list will be added at index 0 of the list
    :return: a tagged list

    >>> list_tagger([])
    [0]
    >>> list_tagger([1, 2, 3])
    [3, 1, 2, 3]
    >>> list_tagger(['apple', 'orange', 'banana'])
    [3, 'apple', 'orange', 'banana']
    """
    batch.insert(0, len(batch))
    return batch


def cutoff(nums, div):
    """
    Count the multiples of a number in a list.

    :param nums: a list of integers
    :param div: an integer
    :precondition: nums must be a list of integers
    :precondition: div must be an integer
    :postcondition: the number of multiples of div in the list will be returned
    :return: an integer that represents the number of multiples in the list

    >>> cutoff([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 3)
    3
    >>> cutoff([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 10)
    0
    >>> cutoff([], 8)
    0
    """
    count = 0
    if div != 0:
        for num in nums:
            count += 1 if num % div == 0 and num >= div else 0
    return count


def prepender(los, s):
    """
    Prepend a string to each string in a list of strings.

    Modifies the list in place and returns None.
    :param los: a list of strings
    :param s: a string
    :precondition: los must be a list of strings
    :precondition: s must be a string
    :postcondition: s will be prepended to each string in the list of strings
    """
    for i in range(len(los)):
        los[i] = s + los[i]


def name_list():
    """
    Create a dictionary of names organized by name length.

    Type "quit" to end the function.
    :postcondition: a dictionary of names will be made
    :return: the dictionary of names organized by name length
    """
    name_dict = {}
    while True:
        name = input("Enter a name:")
        if name == "quit":
            break
        length = len(name)
        name = name.title()
        if length in name_dict.keys():
            name_dict[length].append(name)
        else:
            name_dict[length] = [name]
    return name_dict


def multiples_of_3(upper_bound):
    """
    Sum the multiples of 3 that are less than a specified upper bound.

    :param upper_bound: an integer
    :precondition: upper_bound must be an integer
    :postcondition: the multiples of 3 below the upper bound will be summed
    :return: the sum of the multiples of 3 below the upper bound

    >>> multiples_of_3(0)
    0
    >>> multiples_of_3(10)
    18
    """
    total = 0
    for num in range(0, upper_bound, 3):
        total += num
    return total


def roll_die():
    """
    Simulate a die being rolled and print the results.

    :postcondition: the number of rolls for each side will be printed
    """
    number_of_sides = int(input("Enter the number of sides on the die: "))
    number_of_rolls = int(input("Enter the number of rolls: "))
    result = {side + 1: 0 for side in range(number_of_sides)}
    while number_of_rolls != 0:
        roll = random.randint(1, number_of_sides)
        result[roll] += 1
        number_of_rolls -= 1
    for side in result.keys():
        print(f"{side} was rolled {result[side]} time(s)")
    return
