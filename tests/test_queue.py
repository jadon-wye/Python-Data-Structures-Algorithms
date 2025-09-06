import pytest
from data_structures.queue import Queue
from data_structures.queue_apps import simulate_queue

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


# -------- queue_apps Test --------
def test_simulate_queue_empty_serve_raises():
    # 기본: 빈 큐 예외
    with pytest.raises(IndexError):
        simulate_queue([("serve",)])

def test_simulate_queue_simple_fifo():
    # 단순 흐름: 순차 도착 -> 순차 처리
    result = simulate_queue([("arrive","A"),("arrive","B"),("arrive","C"),("serve",),("serve",),("serve",)])

    assert result["served"] == ["A","B","C"]
    assert result["remaining"] == []

def test_simulate_queue_interleaved():
    # 교차 흐름: 도착/처리 섞임
    result = simulate_queue([("arrive","A"),("arrive","B"),("serve",),("arrive","C"),("serve",),("serve",)])

    assert result["served"] == ["A","B","C"]
    assert result["remaining"] == []

def test_simulate_queue_partial_serve_leaves_remaining():
    # 부분 처리: 남는 항목 확인
    result = simulate_queue([("arrive","A"),("arrive","B"),("arrive","C"),("serve",),("serve",)])

    assert result["served"] == ["A", "B"]
    assert result["remaining"] == ["C"]

def test_simulate_queue_peek_does_not_change_state():
    # peek: 상태 불변
    result = simulate_queue([("arrive","A"),("arrive","B"),("peek",),("serve",)])

    assert result["log"] == ["A"]
    assert result["served"] == ["A"]
    assert result["remaining"] == ["B"]
    assert len(result["remaining"]) == 1

def test_simulate_queue_various_types():
    # 타입 다양성
    result = simulate_queue([("arrive",1),("arrive","py"),("arrive",(1,2)),("serve",),("serve",),("serve",)])

    assert result["served"] == [1,"py",(1,2)]
    assert result["remaining"] == []
