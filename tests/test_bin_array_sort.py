from algorithms.bin_array_sort import bin_array_sort_v4

def test_basic_cases():
    assert bin_array_sort_v4([]) == []
    assert bin_array_sort_v4([1]) == [1]
    assert bin_array_sort_v4([0,1,0]) == [0,0,1]

def test_sorted_random_zeros_ones():
    arr = [0,1,1,0,1,0,0,1]
    assert bin_array_sort_v4(arr[:]) == sorted(arr)