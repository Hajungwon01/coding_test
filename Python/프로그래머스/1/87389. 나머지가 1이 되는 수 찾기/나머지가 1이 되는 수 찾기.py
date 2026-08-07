def solution(n):
    answer = 0
    
    cnt = 1
    
    while True:
        if n % cnt == 1:
            break
        cnt += 1
        
    answer = cnt
        
    return answer