import math

def solution(progresses, speeds):
    answer = []
    
    remain = []
    
    for i in range(len(progresses)):
        remain.append(math.ceil((100-progresses[i])/speeds[i]))
    
    tmp = remain[0]
    count = 0
    for i in range(len(remain)):
        if remain[i] <= tmp:
            count += 1
        else:
            answer.append(count)
            count = 1
            tmp = remain[i]
        if i == len(remain)-1:
            answer.append(count)
    
    return answer