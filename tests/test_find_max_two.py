from algorithms.find_max_two import find_max_two

def test_normal_and_duplicates():
    assert find_max_two([3, -1, 5, 0, 7, 4, 9, 1]) == [9, 7]
    assert find_max_two([9, 9, 1]) == [9, 9]

def test_negatives_and_short():
    assert find_max_two([-5, -2, -9]) == [-2, -5]