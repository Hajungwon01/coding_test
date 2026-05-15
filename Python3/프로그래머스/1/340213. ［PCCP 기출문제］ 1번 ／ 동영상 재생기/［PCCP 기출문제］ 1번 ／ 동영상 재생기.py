def solution(video_len, pos, op_start, op_end, commands):
    # 'MM:SS' 문자열을 총 '초(seconds)'로 변환하는 보조 함수
    def to_seconds(time_str):
        m, s = map(int, time_str.split(':'))
        return m * 60 + s

    # '초'를 다시 'MM:SS' 문자열로 변환하는 보조 함수
    def to_string(seconds):
        m = seconds // 60
        s = seconds % 60
        return f"{m:02d}:{s:02d}"

    # 모든 시간 문자열을 초 단위 정수로 변환
    video_len_sec = to_seconds(video_len)
    pos_sec = to_seconds(pos)
    start_sec = to_seconds(op_start)
    end_sec = to_seconds(op_end)

    # 1. 시작할 때 이미 오프닝 구간에 있는지 먼저 확인
    if start_sec <= pos_sec <= end_sec:
        pos_sec = end_sec

    # 2. 명령어 순차적 수행
    for command in commands:
        if command == "next":
            pos_sec += 10
            if pos_sec > video_len_sec:
                pos_sec = video_len_sec
        elif command == "prev":
            pos_sec -= 10
            if pos_sec < 0:
                pos_sec = 0
        
        # 명령어를 수행한 직후에도 오프닝 구간에 걸치는지 확인
        if start_sec <= pos_sec <= end_sec:
            pos_sec = end_sec

    return to_string(pos_sec)