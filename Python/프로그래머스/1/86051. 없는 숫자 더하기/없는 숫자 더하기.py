def solution(numbers):
    answer = -1
    
    s = set(numbers)
    
    num = set([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])
    
    result = num - s
    
    answer = sum(result)
    
    return answer