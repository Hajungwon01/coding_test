def solution(id_list, report, k):
    answer = [0] * len(id_list)
    id_dict = {id: i for i, id in enumerate(id_list)}
    
    # 중복 제거가 핵심!
    report = list(set(report))
    
    # 피신고자: {신고당한 횟수, 신고한 사람 목록}
    reported_count = {}   # 피신고자별 신고 횟수
    report_by = {}        # 신고자별 신고한 피신고자 목록

    for r in report:
        user1, user2 = r.split(' ')  # user1이 user2를 신고
        reported_count[user2] = reported_count.get(user2, 0) + 1
        if user1 not in report_by:
            report_by[user1] = []
        report_by[user1].append(user2)

    for reporter, reported_list in report_by.items():
        for reported in reported_list:
            if reported_count.get(reported, 0) >= k:
                answer[id_dict[reporter]] += 1

    return answer