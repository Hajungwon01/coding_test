def solution(rsp):
    rule = {"2":"0", "0":"5", "5":"2"}
    answer = ''
    
    for g in rsp:
        answer += rule[g]
    return answer