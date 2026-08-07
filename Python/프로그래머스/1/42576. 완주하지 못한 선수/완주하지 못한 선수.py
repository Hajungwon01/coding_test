from collections import Counter

def solution(participant, completion):
    answer = ''
     
    counter1 = Counter(participant)
    counter2 = Counter(completion)
    
    answer = list((counter1 - counter2).elements())[0]
    
    return answer