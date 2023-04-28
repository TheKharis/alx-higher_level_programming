#!/usr/bin/python3
"""
Find a peak in a list of unsorted integers.

Args:
    list_of_integers (list): list of integers to search for a peak.

Returns:
    int: a peak value in the list.

Complexity:
    O(log(n)) - Binary search algorithm.

"""


def find_peak(list_of_integers):
    if not list_of_integers:
        return None

    left = 0
    right = len(list_of_integers) - 1

    while left < right:
        mid = (left + right) // 2
        if list_of_integers[mid] < list_of_integers[mid + 1]:
            left = mid + 1
        else:
            right = mid

    return list_of_integers[left]
