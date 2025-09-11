'''
Linked List 구현

데이터를 연속된 메모리 공간에 저장하지 않고,
각 데이터가 다음 데이터의 위치를 가리키는 방식으로 구성된 선형 자료 구조
'''
from typing import Any

class Node:
    '''
    연결 리스트의 각 데이터 단위
    '''
    def __init__(self, data: Any):
        self.data = data
        self.next = None

class LinkedList:
    '''
    단일 연결 리스트 자료구조
    '''
    def __init__(self):
        '''
        Linked List 초기화 메서드

        속성: head, size
        '''
        self.head = None
        self.size = 0
    
    def __len__(self) -> int:
        '''
        현재 저장된 원소의 개수를 반환한다.

        Returns
        -------
        int >> 현재 연결 리스트의 길이

        Notes
        -----
        시간복잡도: O(1)
        '''
        return self.size
    
    def __iter__(self):
        '''
        for x in linked_list: 가 가능하게 하는 메서드

        Yields
        -------
        Any >> 연결 리스트의 각 data 값 (반복자)

        Notes
        -----
        시간복잡도: O(n)
        '''
        node = self.head
        while node:
            yield node.data
            node = node.next

    def append(self, value: Any):
        '''
        연결 리스트의 마지막에 value를 추가한다.

        Parameters
        ----------
        value: Any >> 추가할 값

        Notes
        -----
        시간복잡도: O(n)
        '''
        if self.head:
            node = self.head
            while node.next:
                node = node.next
            node.next = Node(value)
            
        else:
            self.head = Node(value)
        self.size += 1

    def prepend(self, value: Any):
        '''
        연결 리스트의 맨 앞에 value를 추가한다.

        Parameters
        ----------
        value: Any >> 추가할 값

        Notes
        ----
        시간복잡도: O(1)
        '''
        if self.head:
            node = Node(value)
            node.next = self.head
            self.head = node

        else:
            self.head = Node(value)
        self.size += 1

    def insert(self, index: int, value: Any):
        '''
        주어진 index 위치에 value를 삽입한다.
        임의의 노드를 생성하여 중간에 노드를 연결한다.

        Parameters
        ----------
        index: int >> 인덱스 (0 <= index <= self.size)
        value: Any >> 추가할 값

        Raises
        -----
        IndexError >> 인덱스가 범위를 벗어난 경우

        Notes
        -----
        시간복잡도: O(n)

        '''
        if self.head is None and index == 0:
            self.head = Node(value)
            self.size += 1

        elif index == 0:
            node = Node(value)
            node.next = self.head
            self.head = node
            self.size += 1

        elif 0 < index <= self.size:
            tmp = Node(value)
            node = self.head
            for _ in range(index - 1):
                node = node.next
            tmp.next = node.next
            node.next = tmp
            self.size += 1

        else:
            raise IndexError(f"Index out of range: {index}")

    def delete(self, value: Any):
        '''
        주어진 value값이 있는 노드를 삭제한다.
        이전 노드를 탐색하여 value 노드의 다음에 연결한다.
        리스트에서 처음 등장하는 노드 하나만 삭제한다.
        값이 없으면 ValueError

        Parameters
        ----------
        value: Any >> 삭제할 값

        Raises
        -----
        ValueError >> 빈 리스트인 경우, 삭제하고자 하는 값이 없는 경우

        Notes
        -----
        시간복잡도: O(n)
        '''
        if self.head is None: # 빈 리스트면 ValueError 발생
            raise ValueError(f"'{value}' is not in Linked List")
        elif value in self:
            prev = None
            node = self.head
            while node.data != value:
                prev = node
                node = node.next
            if prev is None:
                self.head = node.next
            else:
                prev.next = node.next
            self.size -= 1
            
        else:
            raise ValueError(f"'{value}' is not in Linked List")


    def find(self, value: Any) -> int:
        '''
        주어진 value값이 있는 위치를 찾아 반환하는 함수

        Parameters
        ----------
        value: Any >> 찾을 값

        Raises
        ------
        ValueError >> 마지막까지 순회했는데도 찾고자 하는 값이 없는 경우

        Notes
        -----
        시간복잡도: O(n)
        '''
        idx = 0
        node = self.head
        while node:
            if node.data == value:
                return idx
            idx += 1
            node = node.next

        raise ValueError(f"'{value}' is not in Linked List")