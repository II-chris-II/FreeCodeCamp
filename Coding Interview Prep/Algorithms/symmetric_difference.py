# IN PROGRESS

def sym(*args):
    sym_diff = []
    pass

def helper(l1, l2):
    l1 = set(l1)
    l2 = set(l2)

if __name__ == "__main__":

    assert sym([1, 2, 3], [5, 2, 1, 4]) == [3, 4, 5]
    assert sym([1, 2, 3, 3], [5, 2, 1, 4]) == [3, 4, 5]
    assert sym([1, 2, 3], [5, 2, 1, 4, 5]) == [3, 4, 5]
    assert sym([1, 2, 5], [2, 3, 5], [3, 4, 5]) == [1, 4, 5]
    assert sym([1, 1, 2, 5], [2, 2, 3, 5], [3, 4, 5, 5]) == [1, 4, 5]
    assert sym([3, 3, 3, 2, 5], [2, 1, 5, 7], [3, 4, 6, 6], [1, 2, 3]) == [2, 3, 4, 6, 7]
    assert sym([3, 3, 3, 2, 5], [2, 1, 5, 7], [3, 4, 6, 6], [1, 2, 3], [5, 3, 9, 8], [1]) == [1, 2, 4, 5, 6, 7, 8, 9]
    print('Asserts completed.')

