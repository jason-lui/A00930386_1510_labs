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
    >>> list_tagger(["apple", "orange", "banana"])
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


