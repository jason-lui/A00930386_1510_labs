import doctest


"""
We cannot return the length of a sparse vector that is formatted as a dictionary.
The dictionary contains only non-zero values, so it does not show how many zeroes there were
in the original sparse vector. We need to ask the team lead to create a new dictionary entry
that represents the total number of zeroes in the original sparse vector.
"""


def sparse_add(vector_1, vector_2):
    """
    Add two vectors together.

    :param vector_1: a list of integers
    :param vector_2: a list of integers
    :precondition: vector_1 must be a list of integers
    :precondition: vector_2 must be a list of integers
    :postcondition: the vectors will be added together
    :return: a dictionary representing the combined vectors.

    >>> sparse_add({}, {0:1, 2:2, 4:3})
    {0: 1, 2: 2, 4: 3}
    >>> sparse_add({0:1, 2:2, 4:3}, {0:1, 1:3, 2:2, 3:3, 4:3, 5:9})
    {0: 2, 1: 3, 2: 4, 3: 3, 4: 6, 5: 9}
    """
    new_dict = {}

    # Put all entries into vector_1
    for key in vector_2.keys():
        if key in vector_1:
            vector_1[key] += vector_2[key]
        else:
            vector_1[key] = vector_2[key]

    # Reorder the entries in memory
    for key in sorted(vector_1.keys()):
        new_dict[key] = vector_1[key]

    return new_dict


if __name__ == '__main__':
    doctest.testmod()
