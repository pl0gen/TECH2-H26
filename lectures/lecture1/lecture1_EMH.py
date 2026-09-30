"""
Part 2, Lecture 1

Implement and test an argmax() function that returns the location of a maximum.

Tasks
-----

1.  Implement a function argmax() that takes a sequence of numbers and returns
    the index (position) of the maximum element.

2.  Test the function with the following sequence of numbers:
    [2, 3, -1, 7, 4]

3.  Add error handling if an empty sequence is passed. Test the function with an
    empty sequence.

4.  Use the notebook lecture1.ipynb to benchmark your implementation
    against NumPy's argmax().
"""

import numpy as np


def argmax(values):
    """
    Docstring for argmax
    Return the index of the maximum value in a collect.
    Paramters
    ---------
    Values
        Sequence of values

    Return
    -------
    imax: int
        Index of maximum
    """
    N = len(values)

    imax = -1
    # set the vmax to lowest possible value
    vmax = -np.inf

    for i in range(N):
        # first iteration: value=2
        value = values[i]
        # check wheter this valie is larger than any previous
        if value > vmax:
            # update the index and the vmax
            imax = i
            vmax = value

    return imax


values = [2, 3, -1, 7, 4]
print(f'The maximum is located at: {argmax(values)}')


print(np.argmax(values))
