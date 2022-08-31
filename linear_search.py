# Must be a finite list.
# The list must be an integer list.
# Returns true if target is in list.
# Worst case is O(n), where n is the list length
def linear_search(list, target):
    for i in range(len(list)):
        if list[i] == target:
            return True
    return False
