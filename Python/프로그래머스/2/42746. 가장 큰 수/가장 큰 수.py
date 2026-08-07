def solution(numbers):
    answer = ''
    
    tmp = []
    
    for num in numbers:
        tmp.append(str(num))

    tmp.sort(key=lambda x: x * 3, reverse=True)
    
    answer = ''.join(tmp)
    
    return '0' if answer[0] == '0' else answer