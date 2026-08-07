def dec_to_third(n):
    tmp = ''
    while n > 0:
        tmp += str(n%3)
        n //= 3

    return tmp


def solution(n):
    answer = int(dec_to_third(n), 3)
    return answer