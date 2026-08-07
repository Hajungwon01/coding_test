def solution(n, words):
    answer = []
    tmp = ''
    error = False
    tmp_list = []
    
    for i, word in enumerate(words):
        if i == 0 : 
            tmp = word[-1]
            tmp_list.append(word)
            continue
        else:
            if tmp == word[0]:
                if word in tmp_list:
                    error = True
                    answer = [i%n+1, i//n+1]
                    break
                else:
                    tmp = word[-1]
                    tmp_list.append(word)
            else:
                error = True
                answer = [i%n+1, i//n+1]
                break
    
    if error == False:
        answer = [0, 0]
    
    return answer