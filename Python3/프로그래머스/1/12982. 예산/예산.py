def solution(d, budget):
    answer = 0
    
    tmp = 0
    cnt = 0
    
    d.sort()
    
    i = 0
    
    for i in range(len(d)):
        tmp += d[i]
        cnt += 1
        if tmp > budget:
            tmp -= d[i]
            cnt -= 1
            break
        elif tmp == budget:
            break
    
    answer = cnt
    
    return answer