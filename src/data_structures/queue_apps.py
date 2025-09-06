from data_structures.queue import Queue

def simulate_queue(events: list[tuple]) -> dict:
    '''
    이벤트 리스트를 받아 큐 연산을 순차적으로 수행하고,
    처리 결과를 딕셔너리 형태로 반환한다.
    '''
    q = Queue()
    result = {"served": [], "remaining": [], "log": []}

    for i in range(len(events)):
        if events[i][0] == 'arrive':
            q.enqueue(events[i][1])
        elif events[i][0] == 'serve':
            result["served"].append(q.dequeue())
        elif events[i][0] == 'peek':
            result["log"].append(q.front())
    
    result["remaining"] = list(q.buffer)

    return result