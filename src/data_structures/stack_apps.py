from data_structures.stack import Stack

def is_valid_parentheses(s: str) -> bool:
    '''
    Stack 응용 - 괄호 유효성 검사 (Valid Parentheses)
    목표: 문자열의 괄호 ()[]{}가 올바르게 짝을 이루는지 판별.

    규칙
    - 여는 괄호: stack에 push
    - 닫는 괄호: stack의 peek와 짝이 맞으면 pop, 아니면 False
    - 문자열 전체를 확인한 후 stack이 비어 있으면 True
    '''
    stack = Stack()
    open_close = {'(': ')', '{': '}', '[': ']'}

    for i in s:
        if i in open_close:
            stack.push(i)
        elif not stack.is_empty() and i in open_close.values():
            if i == open_close[stack.peek()]:
                stack.pop()
            elif i != open_close[stack.peek()]:
                return False
            else:
                continue
    
    return stack.is_empty()