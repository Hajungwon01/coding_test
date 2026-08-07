def solution(array, commands):
    answer = []
    
    for command in commands:
        substr = array[command[0]-1:command[1]]
        answer.append(sorted(substr)[command[2]-1])
    return answer