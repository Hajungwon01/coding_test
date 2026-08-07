from itertools import combinations

def is_prime_number(num):
    answer = True
    
    if num <= 1:
        return answer
    else:
        for i in range(2, num):
            if num % i == 0:
                answer = False
                return answer
    return answer
    
def solution(nums):
    answer = 0

    for comb in combinations(nums, 3):
        total = sum(comb)
        if is_prime_number(total) == True:
            answer += 1
        

    return answer