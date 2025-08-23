'''
Stack 구현

이 모듈은 파이썬 내장 list를 사용하여
후입선출(Last In First Out, LIFO)의 원칙에 따라 Stack 자료구조를 구현한다.
'''
from typing import Any

class Stack():
    '''
    후입선출(Last In First Out, LIFO) 원칙을 따르는 스택 자료구조.

    내부적으로 파이썬 list를 사용하여 구현.
    '''
    def __init__(self):
        '''
        Stack 초기화 메서드

        버퍼를 파이썬 내장 리스트로 설정한다.
        크기 추적은 len(self.buffer)로 수행한다.
        '''
        self.buffer = []

    def push(self, value: Any) -> None:
        '''
        파이썬 내장 append 메소드를 사용하여 끝에 넣기

        Parameters
        ----------
        value: any >> 추가할 값
        '''
        self.buffer.append(value)
    
    def pop(self) -> Any:
        '''
        파이썬 내장 pop 메소드를 사용하여 마지막 요소 빼내기

        Raises
        ------
        IndexError >> stack 내부에 요소가 없을 경우
        '''
        if len(self.buffer) == 0:
            raise IndexError("pop from empty stack")
        
        return(self.buffer.pop())
    
    def peek(self) -> Any:
        '''
        끝 요소 확인 >> buffer[-1]

        Raises
        ------
        IndexError >> stack 내부에 요소가 없을 경우
        '''
        if len(self.buffer) == 0:
            raise IndexError("peek from empty stack")
        
        return(self.buffer[-1])

    def is_empty(self) -> bool:
        '''
        길이가 0인지 확인하여 True, False 반환
        '''
        return len(self.buffer) == 0

    def size(self) -> int:
        '''
        길이 반환
        '''
        return len(self.buffer)