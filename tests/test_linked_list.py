import pytest
from data_structures.linked_list import LinkedList

# ----- 공통 불변식 헬퍼 -----
def assert_invariant(ll):
    assert len(ll) == ll.size

# --- 초기화, 길이, 순회 Test ---
def test_init_empty_list():
    # 빈 리스트 초기화 및 기본 상태 확인
    ll = LinkedList()
    assert len(ll) == 0
    assert list(ll) == []
    assert ll.head is None
    assert_invariant(ll)

def test_iter_yields_all_elements_in_order():
    # 순회 시 모든 원소가 올바른 순서로 반환되는지 확인
    ll = LinkedList()
    for i in [10, 20, 30, 40, 50]:
        ll.append(i)
    li = list(ll)
    for i, val in enumerate(ll):
        assert val == li[i]


# ------ append Test ------
def test_append_on_empty_becomes_head():
    # 빈 리스트에 append 시 head가 올바르게 설정되는지 확인
    ll = LinkedList()
    ll.append(10)

    assert ll.head.data == 10
    assert len(ll) == 1

def test_append_multiple_preserves_order():
    # 여러 번 append 시 순서가 보존되는지 확인
    ll = LinkedList()
    for i in range(5):
        ll.append(i)
    
    assert list(ll) == [0, 1, 2, 3, 4]
    assert len(ll) == 5
    assert_invariant(ll)


# ------ prepend Test ------
def test_prepend_on_empty_becomes_head():
    # 빈 리스트에서 prepend 시 head가 올바르게 설정되는지 확인
    ll = LinkedList()
    ll.prepend(10)

    assert ll.head.data == 10
    assert len(ll) == 1

def test_prepend_shifts_head():
    # prepend 시 기존 head가 뒤로 밀리는지 확인
    ll = LinkedList()
    ll.append(10)
    ll.prepend(5)

    assert ll.head.data == 5
    assert len(ll) == 2


# ------ insert Test ------
def test_insert_into_empty_at_0():
    # 빈 리스트의 0번 인덱스에 insert
    ll = LinkedList()
    ll.insert(0, 10)

    assert list(ll) == [10]
    assert len(ll) == 1
    assert_invariant(ll)

def test_insert_at_head_index_0():
    # 0번 인덱스에 insert 시 head가 바뀌는지 확인
    ll = LinkedList()
    ll.append(10)
    ll.append(20)
    ll.insert(0, 5)

    assert list(ll) == [5, 10, 20]
    assert ll.head.data == 5
    assert_invariant(ll)

def test_insert_in_middle():
    # 중간 인덱스에 insert
    ll = LinkedList()
    for i in [10, 20, 30]:
        ll.append(i)

    ll.insert(1, 15)

    assert list(ll) == [10, 15, 20, 30]
    assert_invariant(ll)

def test_insert_at_tail_equals_append():
    # 마지막 인덱스에 insert 시 append와 동일한 효과인지 확인
    ll = LinkedList()
    ll.append(10)
    ll.append(20)
    ll.insert(len(ll), 30)

    assert list(ll) == [10, 20, 30]
    assert_invariant(ll)

def test_insert_out_of_range_raises():
    # 인덱스 범위 밖에 insert 시 IndexError 발생 확인
    ll = LinkedList()

    with pytest.raises(IndexError):
        ll.insert(-1, 99)
        ll.insert(len(ll)+1, 99)
    assert_invariant(ll)

    
# ------- find Test -------
def test_find_on_empty_raises():
    # 빈 리스트에서 find 시 ValueError 발생 확인
    ll = LinkedList()

    with pytest.raises(ValueError):
        ll.find(99)
    
def test_find_returns_first_index():
    # 중복 값이 있을 때 첫 번째 인덱스를 반환하는지 확인
    ll = LinkedList()
    for i in [10, 20, 20, 30]:
        ll.append(i)

    assert ll.find(20) == 1

def test_find_not_found_raises():
    # 없는 값을 찾을 때 ValueError 발생 확인
    ll = LinkedList()
    ll.append(1)

    with pytest.raises(ValueError):
        ll.find(99)


# ------ delete Test ------
def test_delete_on_empty_raises():
    # 빈 리스트에서 delete 시 ValueError 발생 확인
    ll = LinkedList()

    with pytest.raises(ValueError):
        ll.delete(99)
    assert_invariant(ll)

def test_delete_head():
    # head 노드 삭제 시 head가 올바르게 변경되는지 확인
    ll = LinkedList()
    for i in [10, 20, 30]:
        ll.append(i)
    
    ll.delete(10)

    assert list(ll) == [20, 30]
    assert ll.head.data == 20
    assert len(ll) == 2
    assert_invariant(ll)

def test_delete_middle():
    # 중간 노드 delete
    ll = LinkedList()
    for i in [10, 20, 30]:
        ll.append(i)
    
    ll.delete(20)

    assert list(ll) == [10, 30]
    assert_invariant(ll)

def test_delete_tail():
    # taile 노드 delete
    ll = LinkedList()
    for i in [10, 20, 30]:
        ll.append(i)
    
    ll.delete(30)

    assert list(ll) == [10, 20]
    assert_invariant(ll)

def test_delete_first_occurrence_only():
    # 중복 값이 있을 때 첫 번째 값만 삭제되는지 확인
    ll = LinkedList()
    for i in [10, 20, 20, 30]:
        ll.append(i)

    ll.delete(20)

    assert list(ll) == [10, 20, 30]
    assert_invariant(ll)


# ---- 예외 후 상태 불변 ----
def test_insert_out_of_range_dose_not_mutate():
    # insert 예외 발생 후 상태 불변
    ll = LinkedList()
    ll.append(10)
    prev = list(ll)

    with pytest.raises(IndexError):
        ll.insert(-1, 99)

    assert list(ll) == prev

def test_find_not_found_does_not_mutate():
    # find 예외 발생 후 상태 불변
    ll = LinkedList()
    ll.append(10)
    prev = list(ll)

    with pytest.raises(ValueError):
        ll.find(99)
    
    assert list(ll) == prev

def test_delete_not_found_does_not_mutate():
    # delete 예외 발생 후 상태 불변
    ll = LinkedList()
    ll.append(10)
    prev = list(ll)

    with pytest.raises(ValueError):
        ll.delete(99)
    
    assert list(ll) == prev


# ------ reverse Test -------
def test_reverse_empty():
    # 빈 리스트에서 reverse 시 정상 동작 확인
    ll = LinkedList()

    ll.reverse()

    assert len(ll) == 0

def test_reverse_single():
    # 원소 1개 reverse 시 변화 없음 확인
    ll = LinkedList()
    ll.append(10)

    ll.reverse()

    assert list(ll) == [10]

def test_reverse_two_nodes():
    # 원소 2개 reverse 시 순서 뒤집히는지 확인
    ll = LinkedList()
    ll.append(10)
    ll.append(20)

    ll.reverse()

    assert list(ll) == [20, 10]

def test_reverse_multiple():
    # 여러 원소 reverse 시 순서가 올바르게 뒤집히는지 확인
    ll = LinkedList()
    for i in [10, 20, 30, 40]:
        ll.append(i)

    ll.reverse()

    assert list(ll) == [40, 30, 20, 10]

def test_reverse_twice_returns_original():
    # 두 번 reverse하면 원래 순서로 돌아오는지 확인
    ll = LinkedList()
    for i in [10, 20, 30, 40]:
        ll.append(i)

    ll.reverse()
    ll.reverse()

    assert list(ll) == [10, 20, 30, 40]