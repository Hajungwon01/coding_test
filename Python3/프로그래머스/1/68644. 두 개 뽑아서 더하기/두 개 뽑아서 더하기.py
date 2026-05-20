def solution(numbers):
    result = set()
    
    for number in range(len(numbers)-1):
        for i in range(number+1, len(numbers)):
            result.add(numbers[number]+numbers[i])
    
    answer = sorted(list(result))
            
    return answer