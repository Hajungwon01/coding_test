def minute_operate(e, s):
    e_int = int(e.split(':')[0]) * 60 + int(e.split(':')[1])
    s_int = int(s.split(':')[0]) * 60 + int(s.split(':')[1])
    
    return e_int - s_int

def change_sharp(melody):
    return melody.replace('C#', 'c').replace('D#', 'd').replace('F#', 'f').replace('G#', 'g').replace('A#', 'a')

def solution(m, musicinfos):
    answer = ''
    
    musicinfo_dct = {}
    
    record = []
    
    for i, musicinfo in enumerate(musicinfos):
        s, e, title, info = musicinfo.split(',')
        musicinfo_dct[i] = title
        tmp = minute_operate(e, s)
        info = change_sharp(info)
        if tmp > len(info) :
            info = info * ((tmp//len(info))+1)
        info = info[:tmp]
        if change_sharp(m) in info:
            record.append([tmp, i])
        
    record.sort(key=lambda x: (-x[0], x[1]))
        
    if len(record) == 0:
        answer = '(None)'
    else:
        answer = musicinfo_dct[record[0][1]]
        
    return answer