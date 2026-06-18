def solution(n, arr1, arr2):
    answer = []
    
    tmp_lst = []

    
    for t1, t2 in zip(arr1, arr2):
        tmp = format(t1 | t2, 'b')
        tmp_lst.append(tmp)
    
    for t in tmp_lst:
        tmp = t
        if len(tmp) < n:
            tmp = '0' * (n-len(tmp)) + tmp
        tmp = tmp.replace('1', '#')
        tmp = tmp.replace('0', ' ')
        answer.append(tmp)
        
    
    return answer