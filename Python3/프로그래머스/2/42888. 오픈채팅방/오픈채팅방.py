def solution(record):
    answer = []
    
    nickname_dct = {}
    
    for r in record:
        if r.split(' ')[0] != 'Leave':
            id, nickname = r.split(' ')[1], r.split(' ')[2]
            nickname_dct[id] = nickname
    
    for r in record:
        if r.split(' ')[0] == 'Leave':
            id = r.split(' ')[1]
            answer.append(f'{nickname_dct[id]}님이 나갔습니다.')
        elif r.split(' ')[0] == 'Enter':
            id = r.split(' ')[1]
            answer.append(f'{nickname_dct[id]}님이 들어왔습니다.')
    
    return answer