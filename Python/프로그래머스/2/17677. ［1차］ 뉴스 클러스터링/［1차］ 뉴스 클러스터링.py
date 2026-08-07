from collections import Counter

def solution(str1, str2):
    answer = 0
    
    tmp_str1 = []
    tmp_str2 = []
    
    for i in range(0, len(str1)-1):
        tmp = str1[i:i+2]
        if tmp[0].isalpha() and tmp[1].isalpha():
            tmp_str1.append(tmp.lower())
    
    for i in range(0, len(str2)-1):
        tmp = str2[i:i+2]
        if tmp[0].isalpha() and tmp[1].isalpha():
            tmp_str2.append(tmp.lower())

    counter1 = Counter(tmp_str1)
    counter2 = Counter(tmp_str2)
    
    union = list((counter1 | counter2).elements())
    
    intersection = list((counter1 & counter2).elements())
    
    len_u = len(union)
    len_i = len(intersection)
    
    if len_u == 0:
        answer = 65536
    else:
        answer = int((len_i / len_u) * 65536)
    
    return answer