def solution(n):
    answer = 0
    for i in range(n//2+1):
        answer += 2*i
    return answer