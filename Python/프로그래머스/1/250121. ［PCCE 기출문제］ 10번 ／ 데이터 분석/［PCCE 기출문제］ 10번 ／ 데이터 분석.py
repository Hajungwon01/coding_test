def solution(data, ext, val_ext, sort_by):
    answer = [[]]
    data_analysis = {"code" : 0, "date" : 1, "maximum" : 2, "remain" : 3}

    critic = data_analysis[ext] # 1
    result1 = []
    for d in data:
        if val_ext > d[critic]:
            result1.append(d)
    
    answer = sorted(result1, key = lambda x : x[data_analysis[sort_by]])
    return answer