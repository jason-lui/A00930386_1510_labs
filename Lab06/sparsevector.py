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
    """
    for key in vector_2.keys():
        if key in vector_1:
            vector_1[key] += vector_2[key]
        else:
            vector_1[key] = vector_2[key]

    return vector_1
