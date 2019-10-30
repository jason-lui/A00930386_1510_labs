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


