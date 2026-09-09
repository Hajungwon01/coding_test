def solution(array):
    answer = []
    tmp = sorted(array, reverse=True)[0]
    answer.append(tmp)
    for i in range(len(array)):
        if array[i] == tmp:
            answer.append(i)
    return answer