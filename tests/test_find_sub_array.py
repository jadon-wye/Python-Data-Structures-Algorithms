from algorithms.find_sub_array import find_sub_array_two_pointer_v2

def test_positive_examples():
    assert find_sub_array_two_pointer_v2([1,2,3,7,5], 12) == [2,4]
    assert find_sub_array_two_pointer_v2([1,2,3,4,5,6,7,8,9,10], 15) == [1,5]

def test_not_found():
    assert find_sub_array_two_pointer_v2([1,2,3,4], 0) == [-1]