# 정수로 이루어진 배열이 주어질 때, 가장 큰 두 수를 찾아 [가장 큰 값, 둘째로 큰 값]을 반환하는 함수를 완성하라.

arr = [3, -1, 5, 0, 7, 4, 9, 1]

def find_max_two(arr: list[int]) -> list[int]:
    """
    배열에서 가장 큰 값과 두 번째로 큰 값을 찾아서 반환한다.
    Args:
        arr (list[int]): 정수 리스트, 길이 < 2라면 그냥 arr 리턴
    Returns:
        list[int]: [최댓값, 두 번째 최댓값]
    Time Complexity:
        O(n) - 한 번 순회
    중복 허용 정책:
        [9, 9, 1] -> [9, 9]
    """
    if len(arr) < 2:
        return arr
    
    max1, max2 = arr[:2]

    if max2 > max1:
        max1, max2 = max2, max1

    for n in arr[2:]:
        if n > max1:
            max1, max2 = n, max1
        elif n > max2:
            max2 = n     

    return [max1, max2]

print(find_max_two(arr))
