'''
Queue 구현

이 모듈은 파이썬 내장 list를 사용하여
선입선출(First In First Out, FIFO)의 원칙에 따라 Queue 자료구조를 구현한다.
'''
from typing import Any

class Queue():
    '''
    선입선출(First In First Out, FIFO) 원칙을 따르는 큐 자료구조.

    내부적으로 파이썬 list를 사용하여 구현.
    '''
    def __init__(self):
        '''
        Queue 초기화 메서드

        버퍼를 파이썬 내장 리스트로 설정한다.
        크기 추적은 len(self.buffer)로 계산한다.
        '''
        self.buffer = []

    def enqueue(self, value: Any) -> None:
        '''
        파이썬 내장 append 메소드를 사용하여 맨 뒤에 값 추가

        Parameters
        ----------
        value: any >> 추가할 값

        Memo
        ----
        시간복잡도: O(1)
        '''
        self.buffer.append(value)
    
    def dequeue(self) -> Any:
        '''
        파이썬 내장 pop 메소드를 사용하여 맨 앞 값 꺼내서 반환

        Raises
        ------
        IndexError >> queue 내부에 요소가 없을 경우

        Memo
        ----
        시간복잡도: O(n)
        '''
        if len(self.buffer) == 0:
            raise IndexError("dequeue from empty stack")
        
        return(self.buffer.pop(0))
    
    def front(self) -> Any:
        '''
        맨 앞 요소 확인 >> buffer[0]

        Raises
        ------
        IndexError >> queue 내부에 요소가 없을 경우

        Memo
        ----
        시간복잡도: O(1)
        '''
        if len(self.buffer) == 0:
            raise IndexError("front from empty stack")
        
        return(self.buffer[0])

    def is_empty(self) -> bool:
        '''
        길이가 0인지 확인하여 True, False 반환

        Memo
        ----
        시간복잡도: O(1)
        '''
        return len(self.buffer) == 0

    def size(self) -> int:
        '''
        길이 반환

        Memo
        ----
        시간복잡도: O(1)
        '''
        return len(self.buffer)