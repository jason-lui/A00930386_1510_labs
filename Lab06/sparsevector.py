import doctest

"""
We cannot return the length of a sparse vector that is formatted as a dictionary.
The dictionary only tracks non-zero values, so it does not show how many zeroes there were
in the original sparse vector. We need to ask the find out the number of zeroes
in the original sparse vector. One way to do this is to change how we store sparse vectors.
We can add another entry that tracks the total number of zeroes. For example,
the sparse vector [1, 0, 0, 0, 0, 0, 1, 0, 2, 0, 0, 0, 0, 0] would be {0: 1 , 6:1, 8: 2, "Zeroes": 11}.
We can determine the length of the sparse vector since we have full information of the original vector.
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

    >>> sparse_add({}, {})
    {}
    >>> sparse_add({}, {0: 1, 2: 2, 4: 3})
    {0: 1, 2: 2, 4: 3}
    >>> sparse_add({0: 1, 2: 2, 99: 3}, {0: 1, 1: 3, 2: 2, 3: 3, 4: 3, 99: 9})
    {0: 2, 2: 4, 99: 12, 1: 3, 3: 3, 4: 3}
    """
    new_dict = {}

    # Put all entries from vector_1 into the new dictionary
    for key, value in vector_1.items():
        new_dict[key] = value

    # Add to or create keys from vector_2
    for key in vector_2:
        if key in vector_1:
            new_dict[key] += vector_2[key]
        else:
            new_dict[key] = vector_2[key]

    # Remove 0 entries
    res = {key: new_dict[key] for key in new_dict if new_dict[key] != 0}
    return res


if __name__ == '__main__':
    doctest.testmod()

