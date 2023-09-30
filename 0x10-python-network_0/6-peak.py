#!/usr/bin/python3
"""
    Function: find_peak(list_of_integers)
"""


def find_peak(list_of_integers):
    """
        finds a peak in a list of unsorted integers
        Args:
            list_of_integers (list)
        Return:
            peak
    """
    list_of_integers = list_of_integers.copy()

    length = len(list_of_integers)

    if length == 0:
        return

    # find index of element in the middle of the list
    mid = int(length/2)

    # compare mid index element with neighbours that is if they exist
    if (mid == 0 or list_of_integers[mid - 1] <= list_of_integers[mid]) and (mid == length - 1
                                                           or list_of_integers[mid + 1]
                                                           < list_of_integers[mid]):
        return list_of_integers[mid]
    elif mid > 0 and list_of_integers[mid - 1] > list_of_integers[mid]:
        return find_peak(list_of_integers[:mid])
    else:
        return find_peak(list_of_integers[mid:])
