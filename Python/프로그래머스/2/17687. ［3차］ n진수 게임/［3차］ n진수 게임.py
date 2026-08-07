check = {10:'A', 11:'B', 12:'C', 13:'D', 14:'E', 15:'F'}

def dec_to_(n, t):
    tmp = ''
    if n == 0: 
        return '0'
    while n > 0:
        num = n % t
        if num >= 10:
            tmp += check[num]
        else:
            tmp += str(num)
        n //= t
    return str(tmp)[::-1]

def solution(n, t, m, p):
    answer = ''
    tmp = '0'
    i = 1
    
    # 길이가 p + mt까지는 최소 되어야
    
    while len(tmp) <= p+m*t:
        tmp += dec_to_(i, n)
        i += 1

    for j in range(0, t):
        answer += tmp[p+j*m-1]
        
    return answer