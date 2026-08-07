def solution(cipher, code):
    answer = ''
    i = 1
    while True:
        tmp = code * i
        if len(cipher) < tmp:
            break
        answer += cipher[tmp-1]
        i += 1
        
    return answer