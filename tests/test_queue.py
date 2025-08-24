import pytest
from data_structures.queue import Queue

# ----- enqueue/dequeue Test ------
def test_enqueue_and_size():
    # 기본 동작
    queue = Queue()
    queue.enqueue(1)
    
    assert queue.size() == 1
    assert not queue.is_empty()

def test_enqueue_dequeue_order():
    # enqueue 여러번, dequeue 여러번 순서 확인
    queue = Queue()
    for i in [10, 20, 30]:
        queue.enqueue(i)

    assert queue.dequeue() == 10
    assert queue.dequeue() == 20
    assert queue.dequeue() == 30
    assert queue.is_empty()


# -------- front Test --------
def test_front_value_and_size():
    # front 값 확인 및 size 변화 없음 확인
    queue = Queue()
    queue.enqueue(10)
    queue.enqueue(20)

    assert queue.front() == 10
    assert queue.size() == 2


# -------- 예외상황 Test --------
def test_dequeue_empty_raises():
    # dequeue 예외상황
    queue = Queue()
    with pytest.raises(IndexError):
        queue.dequeue()

def test_front_empty_raises():
    # front 예외 상황
    queue = Queue()
    with pytest.raises(IndexError):
        queue.front()

def test_dequeue_empty_does_not_change_state():
    # dequeue 실행 시 예외상황 발생해도 자료구조에 이상 없는지 확인
    queue = Queue()
    snapshot = list(queue.buffer)
    with pytest.raises(IndexError):
        queue.dequeue()
    assert list(queue.buffer) == snapshot
    assert queue.size() == 0


# ------- 연산 섞기 -------
def test_shuffle_operations():
    # enqueue와 dequeue를 번갈아 수행하며 연산시 순서 이상 없는지 확인
    queue = Queue()
    queue.enqueue("A")
    queue.enqueue("B")
    assert queue.dequeue() == "A"

    queue.enqueue("C")
    assert queue.dequeue() == "B"
    assert queue.dequeue() == "C"
    assert queue.is_empty()




    
