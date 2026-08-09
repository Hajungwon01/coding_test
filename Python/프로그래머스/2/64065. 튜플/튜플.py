from collections import Counter

def solution(s):
    answer = []
    s_to_list = s
    tmp = ''
    
    s_to_list = s_to_list.replace('}', ']')
    s_to_list = s_to_list.replace('{', '[')
    
    s_to_list = eval(s_to_list)   
    s_to_list.sort(key=len)
    
    
    counter1 = Counter(s_to_list[0])
    answer.append(s_to_list[0][0])
    for i in range(1, len(s_to_list)):
        counter2 = Counter(s_to_list[i])
        
        diff = list((counter2 - counter1).elements())
        answer.append(diff[0])
        counter1 = counter2
        
    return answer