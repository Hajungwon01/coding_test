def solution(survey, choices):
    answer = ''

    result = {'A' : 0, 'N' : 0, 'C' : 0, 'F' : 0, 'M' : 0, 'R' : 0, 'T' : 0, 'J' : 0}
    score = {1 : 3, 2 : 2, 3 : 1, 5 : 1, 6 : 2, 7 : 3}

    compare = [['R', 'T'], ['C', 'F'], ['J', 'M'], ['A', 'N']]

    for index in range(len(survey)):
        if choices[index] < 4 :
            result[survey[index][0]] += score[choices[index]]
        elif choices[index] > 4 :
            result[survey[index][1]] += score[choices[index]]
        else:
            continue       
        
    for c in compare:
        if result[c[0]] > result[c[1]]:
            answer += c[0]
        elif result[c[0]] < result[c[1]]:
            answer += c[1]
        else:
            answer += min(c)
    return answer