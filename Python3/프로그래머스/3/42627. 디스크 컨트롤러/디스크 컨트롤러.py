import heapq

def solution(jobs):
    answer = 0
    now = 0       # 현재 시각
    i = 0         # 처리한 작업 개수
    start = -1    # 가장 최근에 시작한 작업의 요청 시각
    waiting = []
    n = len(jobs)
    
    # 1. 작업 번호를 추적하기 위해 인덱스 정보를 추가하여 정렬
    jobs_with_index = [[job[0], job[1], idx] for idx, job in enumerate(jobs)]
    jobs_with_index.sort(key=lambda x: x[0])
    
    completed = 0
    while completed < n:
        # 2. 현재 시점(now)까지 요청된 작업들을 대기 큐에 삽입
        # 힙 정렬 기준: (소요 시간, 요청 시각, 작업 번호)
        for s, l, idx in jobs_with_index:
            if start < s <= now:
                heapq.heappush(waiting, (l, s, idx))
                
        # 3. 대기 큐에 처리할 작업이 있는 경우
        if waiting:
            l, s, idx = heapq.heappop(waiting)
            start = now       # 최근 작업 시작 시각 갱신
            now += l          # 현재 시각 += 소요 시간
            answer += now - s # 반환 시간 누적
            completed += 1
        else:
            # 4. 대기 큐가 비어있으면 첫 작업이면 첫 요청 시각으로, 아니면 1씩 증가
            now = jobs_with_index[0][0] if start == -1 else now + 1
            
    return answer // n