def solution(num, k):
    answer = str(num).find(str(k)) 
    if str(k) in str(num):
        answer += 1
    return answer