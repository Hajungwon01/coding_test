def solution(my_string):
    tmp = ['a', 'e', 'i', 'o', 'u']
    answer = ''
    
    for s in my_string:
        if s in tmp:
            continue
        else:
            answer += s
    return answer