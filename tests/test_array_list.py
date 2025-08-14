import pytest
from data_structures.array_list import ArrayList

# ------- 불변식 Test -------
def assert_invariant(arr: ArrayList):
    # 불변식 0 ≤ length ≤ capacity
    assert 0 <= arr.length <= arr.capacity
    # 읽기 가능해야 함
    for i in range(arr.length):
        _ = arr[i]
    # length 이후의 buffer 범위 안의 값이 None인지 확인
    for i in range(arr.length+1, arr.capacity):
        assert arr.buffer[i] is None


# ------- __init__/__len__ Test -------
def test_init_and_len():
    arr = ArrayList()
    # 초기 용량(capacity) 확인
    assert arr.capacity == 4
    # 초기 길이(len) 확인
    assert len(arr) == 0
    # 빈 리스트에서 인덱스 접근시 예외 발생 확인
    with pytest.raises(IndexError):
        _ = arr[0]
    # 불변식 검증
    assert_invariant(arr)


# ----- __getitem__/__setitem Test -----
def test_getitem_setitem_basic():   
    # 기본 상태(빈 리스트) test
    arr = ArrayList()
    for i in [30, 40, 50]:
        arr.append(i)
    # getitem basic test
    assert arr[0] == 30
    assert arr[1] == 40
    assert arr[2] == 50
    # setitem basic test
    arr[1] = 20
    assert arr[1] == 20
    assert len(arr) == 3
    # 불변식 검증
    assert_invariant(arr)

def test_getitem_out_of_range():    
    # IndexError 정상 작동 확인
    arr = ArrayList()
    for i in [30, 40, 50]:
        arr.append(i)
    with pytest.raises(IndexError):
        _ = arr[-1]     # 음수 인덱스 미지원
    with pytest.raises(IndexError):
        _ = arr[3]      # 유효한 인덱스는 0, 1, 2
    
    # 불변식 검증
    assert_invariant(arr)
    
def test_setitem_out_of_range():    
    # IndexError 정상 작동 확인 
    arr = ArrayList()
    for i in [30, 40, 50]:
        arr.append(i)
    with pytest.raises(IndexError):
        arr[3] = 60     # 유효한 인덱스는 0, 1, 2
    # 불변식 검증
    assert_invariant(arr)


# ------- append Test --------
def test_append_one():  
    # 한번만 추가
    arr = ArrayList()
    arr.append(1)
    assert len(arr) == 1
    assert arr[0] == 1
    assert_invariant(arr)

def test_append_no_expand():    
    # 용량 내에서 여러 개 추가
    arr = ArrayList()
    for i in [10, 20, 30, 40]:
        arr.append(i)
    assert len(arr) == 4
    assert arr.capacity == 4
    assert [arr[i] for i in range(len(arr))] == [10, 20, 30, 40]
    assert_invariant(arr)
    
def test_append_single_expand():   
    # 경계에서 한 번 더 추가 -> 용량 2배 확장
    arr = ArrayList()
    for i in [10, 20, 30, 40]:
        arr.append(i)
    arr.append(50)
    assert len(arr) == 5
    assert arr.capacity == 8
    assert [arr[i] for i in range(len(arr))] == [10, 20, 30, 40, 50]
    assert_invariant(arr)

def test_append_multiple_expand():
    # 여러번 확장 -> 용량 2배씩 확장
    arr = ArrayList()
    for i in range(20): # capacity: 4->8->16->32
        arr.append(i)
    assert len(arr) == 20
    assert arr.capacity == 32
    for i in range(20):
        assert arr[i] == i
    assert_invariant(arr)


# ------- insert Test -------
def test_insert_one():
    pass