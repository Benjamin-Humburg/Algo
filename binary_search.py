import math

# Must be a sorted list (array).
# Must be a finite list.
# The list must be an integer list.
# Returns true or false if target is in list.
# Worst case is O(log n), where n is the list length
def binary_search(list, target):
    first_index = 0
    last_index = len(list) - 1

    while first_index <= last_index:
        # Check & compare middle item
        middle_index = (last_index - first_index) // 2 + first_index
        middle_item = list[middle_index]
        if target == middle_item:
            return True
        elif target > middle_item:
            first_index = middle_index + 1
        else:
            last_index = middle_index - 1

    return False
