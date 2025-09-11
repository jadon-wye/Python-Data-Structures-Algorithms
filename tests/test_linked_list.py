import pytest
from data_structures.linked_list import LinkedList

# ----- 공통 불변식 헬퍼 -----
def assert_invariant(ll):
    assert len(ll) == ll.size

# --- 초기화, 길이, 순회 Test ---
def test_init_empty_list():
    ll = LinkedList()
    assert len(ll) == 0
    assert list(ll) == []
    assert ll.head is None
    assert_invariant(ll)

def test_iter_yields_all_elements_in_order():
    ll = LinkedList()
    for i in [10, 20, 30, 40, 50]:
        ll.append(i)
    li = list(ll)
    pass


# ------ append Test ------
def test_append_on_empty_becomes_head():
    ll = LinkedList()
    ll.append(10)

    assert ll.head.data == 10
    assert len(ll) == 1

def test_append_multiple_preserves_order():
    ll = LinkedList()
    for i in range(5):
        ll.append(i)
    
    assert list(ll) == [0, 1, 2, 3, 4]
    assert len(ll) == 5
    assert_invariant(ll)


# ------ prepend Test ------
def test_prepend_on_empty_becomes_head():
    ll = LinkedList()
    ll.prepend(10)

    assert ll.head.data == 10
    assert len(ll) == 1

def test_prepend_shifts_head():
    ll = LinkedList()
    ll.append(10)
    ll.prepend(5)

    assert ll.head.data == 5
    assert len(ll) == 2


# ------ insert Test ------
def test_insert_into_empty_at_0():
    ll = LinkedList()
    ll.insert(0, 10)

    assert list(ll) == [10]
    assert len(ll) == 1
    assert_invariant(ll)

def test_insert_at_head_index_0():
    ll = LinkedList()
    ll.append(10)
    ll.append(20)
    ll.insert(0, 5)

    assert list(ll) == [5, 10, 20]
    assert ll.head.data == 5
    assert_invariant(ll)

def test_insert_in_middle():
    ll = LinkedList()
    for i in [10, 20, 30]:
        ll.append(i)

    ll.insert(1, 15)

    assert list(ll) == [10, 15, 20, 30]
    assert_invariant(ll)

def test_insert_at_tail_equals_append():
    ll = LinkedList()
    ll.append(10)
    ll.append(20)
    ll.insert(len(ll), 30)

    assert list(ll) == [10, 20, 30]
    assert_invariant(ll)

def test_insert_out_of_range_raises():
    ll = LinkedList()

    with pytest.raises(IndexError):
        ll.insert(-1, 99)
        ll.insert(len(ll)+1, 99)
    assert_invariant(ll)

    
# ------- find Test -------
def test_find_on_empty_raises():
    ll = LinkedList()

    with pytest.raises(ValueError):
        ll.find(99)
    
def test_find_returns_first_index():
    ll = LinkedList()
    for i in [10, 20, 20, 30]:
        ll.append(i)

    assert ll.find(20) == 1

def test_find_not_found_raises():
    ll = LinkedList()
    ll.append(1)

    with pytest.raises(ValueError):
        ll.find(99)


# ------ delete Test ------
def test_delete_on_empty_raises():
    ll = LinkedList()

    with pytest.raises(ValueError):
        ll.delete(99)
    assert_invariant(ll)

def test_delete_head():
    ll = LinkedList()
    for i in [10, 20, 30]:
        ll.append(i)
    
    ll.delete(10)

    assert list(ll) == [20, 30]
    assert ll.head.data == 20
    assert len(ll) == 2
    assert_invariant(ll)

def test_delete_middle():
    ll = LinkedList()
    for i in [10, 20, 30]:
        ll.append(i)
    
    ll.delete(20)

    assert list(ll) == [10, 30]
    assert_invariant(ll)

def test_delete_tail():
    ll = LinkedList()
    for i in [10, 20, 30]:
        ll.append(i)
    
    ll.delete(30)

    assert list(ll) == [10, 20]
    assert_invariant(ll)

def test_delete_first_occurrence_only():
    ll = LinkedList()
    for i in [10, 20, 20, 30]:
        ll.append(i)

    ll.delete(20)

    assert list(ll) == [10, 20, 30]
    assert_invariant(ll)


# ---- 예외 후 상태 불변 ----
def test_insert_out_of_range_dose_not_mutate():
    ll = LinkedList()
    ll.append(10)
    prev = list(ll)

    with pytest.raises(IndexError):
        ll.insert(-1, 99)

    assert list(ll) == prev

def test_find_not_found_does_not_mutate():
    ll = LinkedList()
    ll.append(10)
    prev = list(ll)

    with pytest.raises(ValueError):
        ll.find(99)
    
    assert list(ll) == prev

def test_delete_not_found_does_not_mutate():
    ll = LinkedList()
    ll.append(10)
    prev = list(ll)

    with pytest.raises(ValueError):
        ll.delete(99)
    
    assert list(ll) == prev