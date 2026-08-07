weekend = [6, 7]

def cal_time(time):
    hour = time // 100
    minute = time % 100
    
    minute += 10
    
    if minute >= 60:
        hour +=1
        minute %= 60
    
    return hour * 100 + minute

def solution(schedules, timelogs, startday):
    answer = 0
    
    tmp = []
    
    for timelog in timelogs:
        t = []
        for i in range(len(timelog)):
            if (startday + i - 1) % 7 + 1 in weekend:
                pass
            else:
                t.append(timelog[i])
        tmp.append(t)
  
    for t in range(len(tmp)):
        if any(ele > cal_time(schedules[t]) for ele in tmp[t]):
            pass
        else:
            answer += 1
    return answer