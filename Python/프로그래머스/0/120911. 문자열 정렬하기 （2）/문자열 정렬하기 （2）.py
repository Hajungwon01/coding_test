def solution(my_string):
    answer = ''
    
    my_string = my_string.lower()
    
    answer = ''.join(sorted(list(my_string)))
    return answer