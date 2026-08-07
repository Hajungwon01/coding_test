def solution(citations):
    answer = 0
    citations.sort() # [0, 1, 3, 5, 6]
    n = len(citations)
    
    # i = 0 | 0 >= 5
    # i = 1 | 1 >= 4
    # i = 2 | 3 >= 3
    for i in range(n):
        if citations[i] >= n - i:
            return n - i
        
        
    return answer