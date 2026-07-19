def solution(priorities, location):
    answer = 0
    queue = ['num' + str(i) for i in range(len(priorities))]
    process = []
    mapping = {}
    
    for q, p in zip(queue, priorities):
        mapping[q] = p
    
    target = queue[location]
    
    
    while len(queue) > 0:
        tmp = queue.pop(0)
        if mapping[tmp] == max(priorities):
            process.append(tmp)
            priorities.remove(mapping[tmp])
        else:
            queue.append(tmp)
    
    answer = process.index(target)+1
        
    return answer