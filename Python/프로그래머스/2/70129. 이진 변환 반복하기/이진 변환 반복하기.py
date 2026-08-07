def remove_zero(mystring):
    num = 0
    tmp = ''
    for ms in mystring:
        if ms == '1':
            tmp += ms
        else:
            num += 1
    
    return num, tmp

def solution(s):
    remove_zero_cnt = 0
    binary_cnt = 0
    
    while s != '1':
        if s.find('0') != -1:
            n, s = remove_zero(s)
            remove_zero_cnt += n
        else:
            binary_cnt += 1
            s = str(format(len(s), 'b'))

    answer = [binary_cnt+1, remove_zero_cnt]
    return answer