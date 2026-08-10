import re

def solution(new_id):
    # 1단계
    one_step = new_id.lower()
    
    # 2단계
    two_step = re.sub(r'[^a-z0-9\-_.]', '', one_step)
    
    # 3단계
    three_step = two_step
    while '..' in three_step:
        three_step = re.sub(r'\.\.', '.', three_step) # 정규식이나 replace 모두 가능합니다
    
    # 4단계
    four_step = three_step.strip(".") # strip을 쓰면 코드가 한 줄로 깔끔해집니다
    
    # 5단계
    five_step = "a" if four_step == "" else four_step
    
    # 6단계
    six_step = five_step
    if len(six_step) >= 16:
        six_step = six_step[:15].strip(".") # 16자 이상일 때 자르고, 끝에 점이 있으면 제거
        
    # 7단계 (작성 중이시던 부분에 이어 하실 수 있도록 빈칸으로 두었습니다)
    seven_step = six_step
    if len(seven_step) <= 2:
        seven_step += seven_step[-1]*3
        seven_step = seven_step[:3]
    

    answer = seven_step
    return answer