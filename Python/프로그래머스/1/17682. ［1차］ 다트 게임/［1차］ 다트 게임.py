def solution(dartResult):
    answer = 0
    tmp = ''
    result = []
    cnt = 0
    
    for dR in list(dartResult):
        if dR == 'S':
            result.append(int(tmp)**1)
            cnt += 1
            tmp = ''
        elif dR == 'D':
            result.append(int(tmp)**2)
            cnt += 1
            tmp = ''
        elif dR == 'T':
            result.append(int(tmp)**3)
            cnt += 1
            tmp = ''
        elif dR == '*':
            result[cnt-1] *= 2
            if cnt-2 >= 0:
                result[cnt-2] *= 2
        elif dR == '#':
            result[cnt-1] *= -1
        else:
            tmp += dR
        
    answer = sum(result)
    print(result)
    
    return answer