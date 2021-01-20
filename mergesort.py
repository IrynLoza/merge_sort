"""Merge sort.

    >>> nums = [3, 5, 10, 2, 1, 9, 7, 6, 4, 8]
    >>> merge_sort(nums)
    >>> nums
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

"""


def merge_sort(lst):
    """Divide and conquer: reduce to lists of 0-1 items, then recombine."""

    if len(lst) < 2:
        return lst
        
    left = []
    right = []
    mid_el = int(len(lst)/2)
    pivot = lst[mid_el]
    center = []

    for el in lst:
        if el < pivot:
            left.append(el)
        elif el > pivot:
            right.append(el)
        else:
            center.append(el)    
 
    return merge_sort(left) + center + merge_sort(right)           

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. AWESOME WORK!\n")
