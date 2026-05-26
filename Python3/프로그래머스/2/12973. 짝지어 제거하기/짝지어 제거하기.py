def solution(s):
    stack = []
    
    for char in s:
        # 1. 스택이 비어있지 않고, 현재 문자가 스택의 맨 위(최근) 문자와 같다면
        if stack and stack[-1] == char:
            stack.pop() # 짝을 찾았으므로 기존 문자도 꺼내서 제거 (Push 안 함)
        # 2. 스택이 비어있거나, 문자가 다르다면
        else:
            stack.append(char) # 스택에 현재 문자 추가
            
    # 3. 모든 문자를 돌았을 때 스택이 텅 비어있으면 성공(1), 남은 게 있으면 실패(0)
    return 1 if not stack else 0