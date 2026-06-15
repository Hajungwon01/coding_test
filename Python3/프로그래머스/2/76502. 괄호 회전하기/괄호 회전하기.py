def check(s):
    s_lst = list(s)
    
    stack = []
    bracket_map = {')': '(', '}': '{', ']': '['}
    
    for char in s_lst:
        if char in bracket_map.values():
            stack.append(char)
        elif char in bracket_map.keys():
            if not stack or stack[-1] != bracket_map[char]:
                return False
            stack.pop()
            
    return len(stack) == 0
        

def solution(s):
    answer = 0
    
    tmp = s
    
    for i in range(len(s)):
        if check(tmp) == True:
            answer += 1
        tmp_lst = list(tmp)
        tmp_lst.insert(0, tmp_lst.pop())
        tmp = ''.join(tmp_lst)
        
    return answer