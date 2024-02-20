def linear_search(lst, target):
    """
    Perform a linear search on the given list to find the target element.
    If found, return its index, otherwise return -1.
    """
    for i in range(len(lst)):
        if lst[i] == target:
            return i
    return -1

# Example usage:
my_list = [1, 5, 3, 8, 2]
target = 8
result = linear_search(my_list, target)
if result == -1:
    print(f"{target} not found in list")
else:
    print(f"{target} found at index {result}")
