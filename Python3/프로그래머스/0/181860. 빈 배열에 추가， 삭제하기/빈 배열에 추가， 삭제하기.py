def solution(arr, flag):
    answer = []
    
    for i in range(len(arr)):
        if flag[i] == True:
            tmp = [arr[i]] * (arr[i] * 2)
            answer += tmp
        elif flag[i] == False:
            for j in range(arr[i]):
                answer.pop()
    
    return answer