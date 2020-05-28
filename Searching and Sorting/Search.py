## execution time   linear_1        linear_2        linear_3        binary_recursive        binary_iterative        list.index
##                  while-loop      for-loop        sentinel        binary                  binary   
## when value is:
## beginning        0.0             0.0             0.0             0.0                     0.0                     0.0
## middle           2379.7          837.5           1243.0          0.0                     0.0                     151.9 
## end              4867.2          1679.0          2482.6          0.0                     0.0                     303.8
## Conclusion: linear search very significanty increases as N increases, suggesting linear time O(N), whereas it can be seen that binary
##             search increases less significantly, indicating logarithmic time O(log_2(N)). list.index likely uses an algorithm that is more
##             optimised than linear but not as efficient than binary, since it cannot assume that the list is sorted

def linear_search_1(lst, value):
    """(list, object) -> int

    Return the index of the first occurrence of value in lst, or return
    -1 if value is not in lst.

    >>> linear_search_1([2, 5, 1, -3], 5)
    1
    >>> linear_search_1([2, 4, 2], 2)
    0
    >>> linear_search_1([2, 5, 1, -3], 4)
    -1
    >>> linear_search_1([], 5)
    -1
    """
    index = 0
    while index < len(lst) and lst[index] != value:
        index += 1
    return index if index < len(lst) else -1

def linear_search_2(lst, value):
    """(list, object) -> int

    Return the index of the first occurrence of value in lst, or return
    -1 if value is not in lst.

    >>> linear_search_2([2, 5, 1, -3], 5)
    1
    >>> linear_search_2([2, 4, 2], 2)
    0
    >>> linear_search_2([2, 5, 1, -3], 4)
    -1
    >>> linear_search_2([], 5)
    -1
    """
    for index in range(0, len(lst)):
        if lst[index] == value:
            return index
    return -1

def linear_search_3(lst, value):
    """(list, object) -> int

    Return the index of the first occurrence of value in lst, or return
    -1 if value is not in lst.

    >>> linear_search_3([2, 5, 1, -3], 5)
    1
    >>> linear_search_3([2, 4, 2], 2)
    0
    >>> linear_search_3([2, 5, 1, -3], 4)
    -1
    >>> linear_search_3([], 5)
    -1
    """
    lst.append(value)
    index = 0
    while lst[index] != value:
        index += 1
    lst.pop(len(lst)-1)
    return index if index < len(lst) else -1

def binary_search_recursive(lst, value, left, right):
    """(list, object, int, int) -> int

    Return the index of the first occurrence of value in lst, or return
    -1 if value is not in lst.

    >>> binary_search_recursive([1, 2, 3], 1, 0, 2)
    0
    >>> binary_search_recursive([1, 2, 3], 2, 0, 2)
    1
    >>> binary_search_recursive([1, 2, 3], 3, 0, 2)
    2
    >>> binary_search_recursive([1, 2, 3], 0, 0, 2)
    -1
    >>> binary_search_recursive([1, 2, 3], 4, 0, 2)
    -1
    >>> binary_search_recursive([1, 2, 3], 4, 0, 2)
    -1
    >>> binary_search_recursive([1, 2, 3], 4, 0, 2)
    -1
    >>> binary_search_recursive([-1, 3, 7], 5, 0, 2)
    -1
    >>> binary_search_recursive([], 1, 0, -1)
    -1
    >>> binary_search_recursive([100], 100, 0, 0)
    0
    >>> binary_search_recursive([-5, -2, -2, 90], -2, 0, 3)
    1
    """
    if right < left:
        return -1
    middle = (left+right)//2
    if lst[middle] == value:
        return middle
    if lst[middle] > value:
        return binary_search_recursive(lst, value, left, middle-1)
    return binary_search_recursive(lst, value, middle+1, right)

def binary_search_iterative(lst, value):
    """(list, object) -> int

    Return the index of the first occurrence of value in lst, or return
    -1 if value is not in lst.

    >>> binary_search_iterative([1, 2, 3], 1)
    0
    >>> binary_search_iterative([1, 2, 3], 2)
    1
    >>> binary_search_iterative([1, 2, 3], 3)
    2
    >>> binary_search_iterative([1, 2, 3], 0)
    -1
    >>> binary_search_iterative([1, 2, 3], 4)
    -1
    >>> binary_search_iterative([1, 2, 3], 4)
    -1
    >>> binary_search_iterative([1, 2, 3], 4)
    -1
    >>> binary_search_iterative([-1, 3, 7], 5)
    -1
    >>> binary_search_iterative([], 1)
    -1
    >>> binary_search_iterative([100], 100)
    0
    >>> binary_search_iterative([-5, -2, -2, 90], -2)
    1
    """
    left = 0
    right = len(lst)-1
    while left <= right:
        middle = (left+right)//2
        if lst[middle] == value:
            return middle
        if lst[middle] > value:
            right = middle-1
        else:
            left = middle+1
    return -1

if __name__ == '__main__':
    import doctest
    doctest.testmod()
