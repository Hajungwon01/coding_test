def solution(numbers):
    mapping = {"zero": 0, "one": 1, "two" : 2, "three" : 3, "four" : 4, "five" : 5, "six" : 6, "seven" : 7, "eight" : 8, "nine" : 9}
    answer = 0
    tmp = numbers
    
    for k in mapping.keys():
        if k in numbers:
            tmp = tmp.replace(k, str(mapping[k]))
            
    answer = int(tmp)
    return answer