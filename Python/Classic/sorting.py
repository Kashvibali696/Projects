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
    if not unsorted:
        return unsorted

    left = []
    right = []
    for index, element in enumerate(unsorted):
        if index % 2 != 0:
            left.append(element)
        else:
            right.append(element)

    left = merge_sort(left)
    right = merge_sort(right)
    return _merge(left, right)


def _merge(left, right):
    merged = []
    while left and right:
        if left[0] <= right[0]:
            merged.append(left.pop(0))
        else:
            merged.append(right.pop(0))

    while left:
        merged.append(left.pop(0))
    while right:
        merged.append(right.pop(0))
    return merged
