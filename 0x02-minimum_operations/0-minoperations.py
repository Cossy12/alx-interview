#!/usr/bin/python3
"""
Minimum Operations
"""


def cprocess(num):
    """
    Calculates minimal operations needed to \
        achieve exactly n H characters in the file.
    """
    div = 1
    c_list = []
    val = num
    while val != 1:
        div += 1
        if val % div == 0:
            while (val % div == 0 and val != 1):
                val /= div
                c_list.append(div)

    return c_list


def minOperations(n):
    if n < 2 or type(n) is not int:
        return 0
    values = cprocess(n)
    return sum(values)
