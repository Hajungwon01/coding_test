def check(n):
    cnt = 0
    for i in range(1, n+1):
        if n % i == 0:
            cnt += 1
            
    return cnt

def solution(left, right):
    answer = 0
    
    for index in range(left, right+1):
        if check(index) % 2 == 0:
            answer += index
        else:
            answer -= index
            
    return answer