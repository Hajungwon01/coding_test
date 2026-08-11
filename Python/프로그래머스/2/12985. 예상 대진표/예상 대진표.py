import math

def cal(target_number):
    # 짝수인 경우 (v2 자리에 위치)
    if target_number % 2 == 0:
        group = target_number // 2
    else:
      # 홀수인 경우 (v1 자리에 위치하므로 1을 더하고 나누기)
        group = (target_number + 1) // 2
    return group

def solution(n,a,b):
    answer = 0
    
    playnum_a = a
    playnum_b = b
    for i in range(int(math.log(n, 2))):
        playnum_a = cal(playnum_a)
        playnum_b = cal(playnum_b)
        if playnum_a == playnum_b:
            answer = i+1
            break
    
    return answer