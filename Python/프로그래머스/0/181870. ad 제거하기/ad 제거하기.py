def solution(strArr):
    answer = []
    
    for str in strArr:
        if not 'ad' in str:
            answer.append(str)
    return answer