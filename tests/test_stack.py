import pytest
from data_structures.stack import Stack

# ------- push/pop Test --------
def test_push_and_size():
    # 기본 동작
    stack = Stack()
    stack.push(0)
    assert stack.size() == 1

def test_push_pop_order():
    # push 여러번, pop 여러번 순서 확인
    stack = Stack()
    for i in [10, 20, 30]:
        stack.push(i)

    assert stack.pop() == 30
    assert stack.pop() == 20
    assert stack.pop() == 10


# -------- peek Test --------
def test_peek_value_and_size():
    # peek 값 확인 및 size 변화 없음 확인
    stack = Stack()
    stack.push(10)
    stack.push(20)

    assert stack.peek() == 20
    assert stack.size() == 2


# ------- is_empty Test -------
def test_is_empty():
    # is_empty 동작 확인
    stack = Stack()
    assert stack.is_empty()

    stack.push(1)
    assert not stack.is_empty()

    stack.pop()
    assert stack.is_empty()


# -------- 예외 상황 Test --------
def test_pop_empty_raises():
    # pop 예외상황
    stack = Stack()
    with pytest.raises(IndexError):
        stack.pop()
    
def test_peek_empty_raises():
    # peek 예외상황
    stack = Stack()
    with pytest.raises(IndexError):
        stack.peek()
    