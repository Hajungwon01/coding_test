def solution(s):
    stack = []
    
    for c in s:
        # 스택의 top과 현재 문자가 같으면 → 짝 제거
        if stack and stack[-1] == c:
            stack.pop()
        # 다르면 → 스택에 push
        else:
            stack.append(c)
    
    return 1 if not stack else 0
