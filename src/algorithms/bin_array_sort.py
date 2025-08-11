# 0과 1로 이루어진 배열이 있다. 배열 자체를 오름차순으로 정렬하라.
# python의 sort() 메소드 구현하기

# Two Pointer 방식으로 구현하기 (1차)
def bin_array_sort_v1(arr: list[int]) -> list[int]:
    """
    0과 1로 이루어진 배열 arr를 오름차순으로 정렬한다.
    Args:
        arr (list[int]): 정수 리스트, 길이 >= 2
    Returns:
        list[int]: [최댓값, 두 번째 최댓값]
    Time Complexity:
        O(n) - 한 번 순회
    """
    left = 0                # left Pointer
    right = len(arr) - 1    # right Pointer

    while left < right:
        if arr[left] == 0:
            left += 1
        if arr[right] == 1:
            right -= 1
        if arr[left] == 1 and arr[right] == 0:
            arr[left], arr[right] = arr[right], arr[left]
        
    return arr

# Two Pointer 방식으로 구현하기 (2차) -> if문 독립시행으로 인한 무한루프 방지
def bin_array_sort_v2(arr: list[int]) -> list[int]:
    """
    Args:
        arr (list[int]): 정수 리스트, 길이 >= 2
    Returns:
        list[int]: [최댓값, 두 번째 최댓값]
    Time Complexity:
        O(n) - 한 번 순회
    """
    left = 0
    right = len(arr) - 1

    while left < right:
        if arr[left] == 0:
            left += 1
        elif arr[right] == 1:
            right -= 1
        else:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
    
    return arr

# Two Pointer 방식으로 구현하기 (3차) -> 반복을 줄여 효율적으로 접근하기
def bin_array_sort_v3(arr: list[int]) -> list[int]:
    """
    Args:
        arr (list[int]): 정수 리스트, 길이 >= 2
    Returns:
        list[int]: [최댓값, 두 번째 최댓값]
    Time Complexity:
        O(n) - 한 번 순회
    """
    left = 0
    right = len(arr) - 1

    while left < right:
        while arr[left] == 0:
            left += 1
        while arr[right] == 1: # IndexError: list index out of range
            right -= 1
        if left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left, right = left + 1, right - 1
    
    return arr

# Two Pointer 방식으로 구현하기 (4차) -> 오류 제거
def bin_array_sort_v4(arr: list[int]) -> list[int]:
    """
    Args:
        arr (list[int]): 정수 리스트, 길이 >= 2
    Returns:
        list[int]: [최댓값, 두 번째 최댓값]
    Time Complexity:
        O(n) - 한 번 순회
    """
    left = 0
    right = len(arr) - 1

    if any(x not in (0, 1) for x in arr): raise ValueError # 입력 검증 추가

    while left < right:
        while left < right and arr[left] == 0: # left가 right를 넘어 가지 않도록 반복 조건 수정
            left += 1
        while left < right and arr[right] == 1: # 위와 동일
            right -= 1
        if left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left, right = left + 1, right - 1

    return arr

# Counting 방식으로 구현하기 (1차)
def bin_array_sort_counting(arr: list[int]) -> list[int]:
    """
    Args:
        arr (list[int]): 정수 리스트, 길이 >= 2
    Returns:
        list[int]: [최댓값, 두 번째 최댓값]
    Time Complexity:
        O(n) - 한 번 순회
    """
    return [0]*arr.count(0) + [1]*arr.count(1)

# Test code 
for arr in ([1, 0, 1, 1, 1, 1, 1, 0, 0, 0], [1, 1]):  
    print(bin_array_sort_counting(arr))  
    