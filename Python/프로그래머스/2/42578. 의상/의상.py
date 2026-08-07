def solution(clothes):
    answer = 1
    cabinet = dict()
    
    for cloth in clothes:
        if cloth[1] not in cabinet.keys():
            cabinet[cloth[1]] = [cloth[0]]
        else:
            cabinet[cloth[1]].append(cloth[0])
    
    for key in cabinet.keys():
        answer *= (len(cabinet[key]) + 1)
    answer -= 1
    return answer