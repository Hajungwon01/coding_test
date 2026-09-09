def solution(s1, s2):
    answer = 0
    s1_set = set(s1)
    s2_set = set(s2)
    tmp = s1_set.intersection(s2)
    answer = len(tmp)
    return answer