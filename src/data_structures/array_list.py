'''
ArrayList (동적 배열) 구현

이 모듈은 파이썬 내장 list를 사용하지 않고
동적 배열(ArrayList) 자료구조를 구현한다.
내부 버퍼는 용량(capacity)가 가득 차면 2배로 확장한다.

'''
from typing import Any

class ArrayList():
    '''
    0 ≤ length ≤ capacity
    유효한 값은 buffer[0..length-1] 범위에만 있다.
    '''
    def __init__(self):    # 동적 배열 초기화
        '''
        ArrayList 초기화 메서드.

        초기 용량(capacity) 크기의 버퍼를 설정하고
        길이(length)를 0으로 설정한다. -> 실제 원소가 없음

        Notes
        ------
        초기 capacity는 4로 설정
        시간복잡도: O(1)
        '''
        self.capacity = 4   # 초기 용량 설정
        self.buffer = [None] * self.capacity    # 미리 확보한 용량만큼 빈 칸으로 채우기
        self.length = 0     # 실제 원소가 없기 때문에 0으로 설정

    def __len__(self) -> int:
        '''
        현재 저장된 원소의 개수를 반환한다.

        Returns
        -------
        int >> 현재 리스트의 길이

        Notes
        -----
        시간복잡도: O(1)
        '''
        return self.length
    
    def __getitem__(self, i: int) -> Any:
        '''
        주어진 인덱스 i에 해당하는 원소를 반환한다.

        Parameters
        ---------
        i: int >> 인덱스 (0 <= i < length)

        Returns
        -------
        Any >> 해당 인덱스의 원소

        Raise
        ------
        IndexError >> 인덱스가 범위를 벗어난 경우
        
        Notes
        -----
        시간복잡도: O(1)
        '''
        if 0 <= i < self.length:
            return self.buffer[i]
        else:
            raise IndexError(f"index out of range: {i}")
    
    def __setitem__(self, i: int, value) -> None:
        '''
        주어진 인덱스 i에 해당하는 원소의 값을 value로 바꾼다.

        Parameters
        ----------
        i: int >> 인덱스 (0 <= i < self.length)
        value: any >> 변경할 값

        Raise
        -----
        IndexError >> 인덱스가 범위를 벗어난 경우

        Notes
        -----
        시간복잡도: O(1)
        '''
        if 0 <= i < self.length:
            self.buffer[i] = value
        else:
            raise IndexError(f"index out of range: {i}")

    def append(self, value: Any) -> None:                                        # append 메소드 구현
        '''
        리스트의 마지막에 value를 추가한다.
        버퍼가 가득 찬 경우 capacity를 2배 확장한다.

        Parameters
        ----------
        value: any >> 추가할 값

        Notes
        -----
        시간복잡도: O(1)
        확장 발생시: O(n)
        + new_capacity와 new_buffer은 속성화할 필요 없다.
        '''
        if self.length == self.capacity:                            # 길이가 용량과 같아졌을 경우 용량 확장
            new_capacity = self.capacity * 2                        # 지역변수 new_capacity를 설정하여 확장된 용량 저장
            new_buffer = [None] * new_capacity                      # 지역변수 new_buffer을 설정하여 확장된 버퍼 저장
            for i in range(self.length):                            # 기존 버퍼를 new_buffer에 복제
                new_buffer[i] = self.buffer[i]  
            self.buffer, self.capacity = new_buffer, new_capacity   # 기존 속성(buffer, capacity)에 새로 설정한 버퍼와 용량 저장 

        self.buffer[self.length] = value    # 기존 append 메소드 역할
        self.length += 1


    def insert(self, index: int, value: Any) -> None:
        '''
        주어진 index 위치에 value를 삽입한다.
        index 이후의 원소들은 1씩 밀려난다.

        Parameters
        ----------
        index: int >> 인덱스 (0 <= index <= self.length)
        value: Any >> 추가할 값

        Raises
        -----
        IndexError >> 인덱스가 범위를 벗어난 경우

        Notes
        -----
        시간복잡도: O(n)

        '''
        if 0 <= index <= self.length:
            if self.length == self.capacity:    # append 메소드와 동일하게 length == capacity일 경우 용량 확장
                new_capacity = self.capacity * 2
                new_buffer = [None] * new_capacity               
                for i in range(self.length):                           
                    new_buffer[i] = self.buffer[i]  
                self.buffer, self.capacity = new_buffer, new_capacity
                
            for i in range(self.length, index, -1):
                self.buffer[i] = self.buffer[i-1]
            self.buffer[index] = value
            self.length += 1
        else:
            raise IndexError(f"index out of range: {index}")
