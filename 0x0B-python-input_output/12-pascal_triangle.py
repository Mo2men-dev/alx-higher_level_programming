#!/usr/bin/python3
"""pascal triangle using list of lists module"""


def pascal_tri(n):
    """
    prints the pascal triangle

    Args:
        n (int): number of rows to be printed

    Returns:
        None
    """
    o = [[1], [1, 1]]
    for i in range(1, n - 1):
        temp = []
        temp.append(1)

        for j in range(len(o[i]) - 1):
            temp.append(o[i][j] + o[i][j + 1])

        temp.append(1)
        o.append(temp)

    return o
