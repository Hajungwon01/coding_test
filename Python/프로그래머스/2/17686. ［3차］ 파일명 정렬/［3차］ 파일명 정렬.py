def split_filename(s):
    head = ''
    number = ''
    
    for i in range(len(s)):
        if s[i].isdigit():
            head = s[:i]
            number = s[i:]
            break
    
    for j in range(len(number)):
        if not number[j].isdigit():
            number = number[:j]
            break

    return head, number

def solution(files):
    answer = []
    
    split_list = []
    
    for i, file in enumerate(files):
        tmp = split_filename(file)
        split_list.append([tmp[0].lower(), int(tmp[1]), i])
    
    split_list = sorted(split_list, key=lambda x: (x[0], x[1], x[2]))
    
    for s in split_list:
        answer.append(files[int(s[2])])
                
    return answer