def solution(cards1, cards2, goal):
    answer = ''
    while len(goal) != 0:
        if len(cards1) > 0 and goal[0] == cards1[0]:
            del  goal[0]
            del cards1[0]
            continue
        elif len(cards2) > 0 and goal[0] == cards2[0]:
            del goal[0]
            del cards2[0]
            continue
        else:
            answer = 'No'
            break
    
    if answer == '':
        answer = 'Yes'

    return answer 