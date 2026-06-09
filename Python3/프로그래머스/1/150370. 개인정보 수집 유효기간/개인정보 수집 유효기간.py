def date_compare(d1, d2):
    d1_lst = d1.split('.')
    d2_lst = d2.split('.')
    
    
    for i in range(3):
        if int(d1_lst[i]) < int(d2_lst[i]):
            return True
        elif int(d1_lst[i]) == int(d2_lst[i]):
            continue
        else:
            return False
    
    return True
# True는 파기
    
def date_add(d, a):
    # 날짜를 일 단위로 변환
    y, m, day = map(int, d.split('.'))
    total_days = (y * 12 * 28) + (m * 28) + day
    
    # 유효기간(개월)을 더함 (a * 28일)
    # 예: 2021.05.02에 A(6개월)를 더하면 -> 만료일이 2021.11.02가 됨
    expire_days = total_days + ((a-1) * 28)
    
    # 다시 YYYY.MM.DD 형태로 변환하여 반환
    y_new = (expire_days - 1) // (12 * 28)
    m_new = ((expire_days - 1) % (12 * 28)) // 28 + 1
    d_new = (expire_days - 1) % 28 + 1
    
    return f"{y_new:04d}.{m_new:02d}.{d_new:02d}"

def solution(today, terms, privacies):
    answer = []
    
    term_dct = {}
    
    for term in terms:
        t, d = term.split(' ')
        term_dct[t] = int(d)
        
    for i, p in enumerate(privacies):    
        d, t = p.split(' ')
        a = date_add(d, term_dct[t])
        print(a)
        if date_compare(a, today):
            answer.append(i+1)
    return answer