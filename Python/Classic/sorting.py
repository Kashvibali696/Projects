from __future__ import unicode_literals


def bubble_sort(unsorted):
    copy = unsorted[:]

    while True:
        swap_count = 0
        for index, element in enumerate(copy[:-1][:]):
            if element > copy[index + 1]:
                copy[index] = copy[index + 1]
                copy[index + 1] = element
                swap_count += 1

        if not swap_count:
            break
    return copy


def merge_sort(unsorted):
    pass
