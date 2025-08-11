# 정렬되지 않은 양의 정수로 이루어진 배열 A가 있다. 연속된 원소를 더한 값이 제시된 값 S와 같은 부분 배열을 찾아라. (인덱스 기준은 1이다.)
# 입력: arr = [1, 2, 3, 7, 5], s = 12, 출력: [2, 4]
# 인덱스 2부터 4까지의 합: 2 + 3 + 7 = 12
# 입력: arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], s = 15, 출력: [1, 5]

# 이중 for문 방식으로 구현하기 
def find_sub_array_for(arr: list[int], s: int) -> list[int]:
    """
    배열 arr에서 연속한 원소의 합이 s인 부분 배열의 인덱스를 구한다.
    Arguments:
        arr (list[int]): 양의 정수
        s: 부분 배열의 합
    Return:
        list[int]: 부분 배열의 인덱스, 조건을 만족하는 부분 배열이 없으면 [-1]
    Time Complexity:
        O(n²) - 두 번 순회
    """
    for i in range(len(arr)):
        for j in range(i):
            if sum(arr[j:i]) == s:
                return [j+1, i]
        
    return [-1]

# Two Pointer 방식으로 구현하기 (1차)
def find_sub_array_two_pointer_v1(arr: list[int], s: int) -> list[int]:
    """
    Arguments:
        arr (list[int]): 양의 정수
        s: 부분 배열의 합
    Return:
        list[int]: 부분 배열의 인덱스, 조건을 만족하는 부분 배열이 없으면 [-1]
    Time Complexity:
        O(n1) - 한 번 순회
    """
    left = 0
    sub_total = 0

    for right in range(len(arr)):
        # print(right, left, sub_total)
        sub_total += arr[right]         # right를 반복문으로 0~len(arr)까지 돌리며 sub_total에 arr[right] 값을 더함 
        if sub_total == s:              # 같아지면 인덱스 리턴
            return [left+1, right+1]
        elif sub_total > s:             # sub_total값이 s보다 커지면
            sub_total -= arr[left]      # arr[left]값을 빼고
            left += 1                   # left Pointer를 오른쪽으로 이동
    return [-1]     # 반복문이 끝까지 돌 때까지 리턴되지 않으면 -1 리턴
# 결과값: [-1] [1, 5]
# 문제점: 부분합이 s보다 커질 때 한 번만 left를 이동

# Two Pointer 방식으로 구현하기 (2차) -> 부분합이 s보다 커질 때 left가 여러번 이동할 수 있도록 조정
def find_sub_array_two_pointer_v2(arr: list[int], s: int) -> list[int]:
    """
    Arguments:
        arr (list[int]): 양의 정수
        s: 부분 배열의 합
    Return:
        list[int]: 부분 배열의 인덱스, 조건을 만족하는 부분 배열이 없으면 [-1]
    Time Complexity:
        O(n) - 한 번 순회
    """
    if s <= 0:  # 예외처리
        return [-1]
    left = 0
    sub_total = 0

    for right in range(len(arr)):
        sub_total += arr[right]         
        while sub_total > s :
            sub_total -= arr[left]
            left += 1
        if sub_total == s:
            return [left+1, right+1]
    return [-1]

# Test code
sample1 = ([1, 2, 3, 7, 5], 12)
sample2 = ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 15)
sample3 = ([1, 2, 3, 4], 0)
for arr, s in (sample1, sample2, sample3):
    print(find_sub_array_two_pointer_v2(arr, s))