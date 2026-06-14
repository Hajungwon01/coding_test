import math

def calculate_time(s, e):
    tmp = s.split(':')
    s_int = int(tmp[0]) * 60 + int(tmp[1])
    tmp = e.split(':')
    e_int = int(tmp[0]) * 60 + int(tmp[1])
    
    e_s = e_int - s_int
    
    return e_s
    

def calculate_fee(time, fees):
    total = 0
    
    if time > fees[0]:
        total += fees[1] + ((math.ceil((time-fees[0])/fees[2])) * fees[3])
        
    else:
        total = fees[1]
    
    return total
    


def solution(fees, records):
    answer = []
    record_dct = {}
    park = []
    
    for record in records:
        tmp = record.split(' ')
        if tmp[1] not in record_dct:
            record_dct[tmp[1]] = {}
        if tmp[2] == 'IN':
            record_dct[tmp[1]]['start'] = tmp[0]
            park.append(tmp[1])
        else:
            record_dct[tmp[1]]['total_time'] = calculate_time(record_dct[tmp[1]]['start'], tmp[0]) + record_dct[tmp[1]].get('total_time', 0)
            park.remove(tmp[1])
    
    if len(park) != 0:
        for p in park:
            record_dct[p]['total_time'] = calculate_time(record_dct[p]['start'], '23:59') + record_dct[p].get('total_time', 0)
            
    num_lst = sorted(list(record_dct.keys()))
    
    for num in num_lst:
        answer.append(calculate_fee(record_dct[num]['total_time'], fees))
    
    
    return answer