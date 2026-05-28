def solution(msg):
    answer = []
    
    dct = {chr(64 + i): i for i in range(1, 27)}
    
    tmp_n = 0
    tmp_s = ''
    
    left = 0
    right = 0
    
    while left < len(msg):
        tmp_n = 0
        num = len(dct)
        right = left
        while right <= len(msg):
            right += 1
            tmp_s = msg[left : right]
            if tmp_s in dct.keys():
                tmp_n = dct[tmp_s]
            else:
                dct[tmp_s] = num + 1
                break
        left = right - 1
        answer.append(tmp_n)
        
    return answer