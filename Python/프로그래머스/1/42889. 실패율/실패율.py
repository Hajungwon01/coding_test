def solution(N, stages):
    answer = []

    dct = {}

    challenger = len(stages)


    for stage in range(N):
        if stages.count(stage+1) == 0:
            dct[stage+1] = 0
        else:
            dct[stage+1] = stages.count(stage+1)/challenger
            challenger -= stages.count(stage+1)

    answer = list(dict(sorted(dct.items(), key = lambda x : x[1], reverse = True)).keys())

    return answer

