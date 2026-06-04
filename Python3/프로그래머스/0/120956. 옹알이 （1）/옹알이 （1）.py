def solution(babbling):
    answer = 0
    can_speak = ["aya", "ye", "woo", "ma"]
    
    for b in babbling:
        tmp = ''
        for c in b:
            tmp += list(c).pop()
            if tmp in can_speak:
                tmp = ''
        if tmp == '':
            answer += 1
    return answer