from Sorting import Sort

def test_selection():
    sort = Sort()
    array: list[int] = [6, 1, 87, 53, 2]
    sort.selection(array)
    assert array == [1, 2, 6, 53, 87]
    array: list[int] = ['o', 'b', 'a', 'q', 'd']
    sort.bubble(array)
    assert array == ['a', 'b', 'd', 'o', 'q']

def test_bubble():
    sort = Sort()
    array: list[int] = [6, 1, 87, 53, 2]
    sort.bubble(array)
    assert array == [1, 2, 6, 53, 87]
    array: list[int] = ['o', 'b', 'a', 'q', 'd']
    sort.bubble(array)
    assert array == ['a', 'b', 'd', 'o', 'q']

def test_insertion():
    sort = Sort()
    array: list[int] = [6, 1, 87, 53, 2]
    sort.insertion(array)
    assert array == [1, 2, 6, 53, 87]
    array: list[int] = ['o', 'b', 'a', 'q', 'd']
    sort.insertion(array)
    assert array == ['a', 'b', 'd', 'o', 'q']

def test_merge():
    sort = Sort()
    array: list[int] = [6, 1, 87, 53, 2]
    sort.merge(array)
    assert array == [1, 2, 6, 53, 87]
    array: list[int] = ['o', 'b', 'a', 'q', 'd']
    sort.merge(array)
    assert array == ['a', 'b', 'd', 'o', 'q']

def test_quick():
    sort = Sort()
    array: list[int] = [6, 1, 87, 53, 2]
    sort.quick(array)
    assert array == [1, 2, 6, 53, 87]
    array: list[int] = ['o', 'b', 'a', 'q', 'd']
    sort.quick(array)
    assert array == ['a', 'b', 'd', 'o', 'q']
    
def test_counting():
    sort = Sort()
    array: list[int] = [1, 0, 3, 1, 3, 1]
    result = sort.counting(array)
    assert result == [0, 1, 1, 1, 3, 3]
    sort = Sort()
    array: list[int] = [6, 1, 87, 53, 2]
    result = sort.counting(array)
    assert result == [1, 2, 6, 53, 87]
    # array: list[int] = ['o', 'b', 'a', 'q', 'd']
    # result = sort.counting(array)
    # assert result == ['a', 'b', 'd', 'o', 'q']
    