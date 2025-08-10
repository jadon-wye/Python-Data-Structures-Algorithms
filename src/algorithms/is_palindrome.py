# 주어진 문자열이 회문이면 True, 회문이 아니면 False를 반환하라.
# 입력: madam, 출력: True
# 입력: tomato, 출력: False

word = "racecar"

# 문자열의 슬라이싱을 이용하기
# if word == word[::-1]:
#     print(True)
# else:
#     print(False)


# 두 포인터(Two Pointers)를 이용한 방법
def is_palindrome(word: str) -> bool:
    """
    문자열 word가 회문(palindrome)인지 검사한다.
    Arguments:
        word (str): 회문인지 검사할 문자열
    Return:
        bool: 회문이면 True, 그렇지 않으면 False를 반환
    """
    word = word.lower().replace(" ", "")    # 대소문자, 공백처리
    pnt1 = 0                # Left Pointer 
    pnt2 = len(word) - 1    # Right Pointer

    while pnt1 < pnt2:      # 각 포인터가 만나기 전까지
        if word[pnt1] != word[pnt2]: # 만약 두 문자가 다르다면
            return False            # False 리턴
        else:
            pnt1 += 1   # Left Pointer는 왼쪽으로 1씩 이동하고
            pnt2 -= 1   # Right Pointer는 오른쪽으로 1씩 이동
    return True

words = ["racecar", "rotor", "tomato", "별똥별", "코끼리", "Madam", "A man a plan a canal Panama"]
for word in words:
    print(f"Is '{word}' palindrome?  {is_palindrome(word)}")