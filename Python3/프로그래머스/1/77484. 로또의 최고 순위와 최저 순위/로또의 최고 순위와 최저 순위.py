def solution(lottos, win_nums):
    rank = {6:1, 5:2, 4:3, 3:4, 2:5, 1:6, 0:6}
    
    lottos_set = set(lottos)
    win_nums_set = set(win_nums)
    
    zero_cnt = 0
    
    tmp = lottos_set.intersection(win_nums_set)
    
    for lotto in lottos:
        if lotto == 0:
            zero_cnt += 1
            
    answer = [rank[len(tmp)+zero_cnt], rank[len(tmp)]]
    return answer