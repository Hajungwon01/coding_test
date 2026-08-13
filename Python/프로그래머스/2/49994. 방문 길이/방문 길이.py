def solution(dirs):
    answer = 0
    move_dict = {"U":[0, 1], "D":[0, -1], "R":[1, 0], "L":[-1, 0]}
    record = []
    
    status = [0, 0]
    
    for dir in dirs:
        start_str = str(status[0]) + str(status[1])
        moved = [status[0] + move_dict[dir][0], status[1] + move_dict[dir][1]]
        if moved[0] < -5 or moved[1] < -5 or moved[0] > 5 or moved[1] > 5:
            continue
        else:
            end_str = str(moved[0]) + str(moved[1])
            if start_str + end_str not in record or end_str + start_str not in record:
                record.append(start_str + end_str)
                record.append(end_str + start_str)
                answer += 1
            status = moved
    return answer