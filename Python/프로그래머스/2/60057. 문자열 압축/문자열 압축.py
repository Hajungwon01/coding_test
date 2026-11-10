def solution(s):
    answer = 0
    
    results = [len(s)]
    
    for i in range(1, len(s)//2+1):
        result = ''
        tmp = ''
        count = 0
        for j in range(0, len(s), i):
            if tmp == s[j:j+i]:
                count += 1
            else:
                if count > 1:
                    result += str(count) + tmp
                else:
                    result += tmp
                tmp = s[j:j+i]
                count = 1
        if count > 1:
            result += str(count) + tmp
        else:
            result += tmp
        results.append(len(result))
    
    answer = min(results)
    return answer