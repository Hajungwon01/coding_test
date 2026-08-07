def solution(s):
    answer = True
    tmp = []
    
    for c in s:
        if c == '(':
            tmp.append('(')
        else:
            if len(tmp) == 0:
                return False
            tmp.pop()
    if len(tmp) > 0:
        answer = False
        
    return answer