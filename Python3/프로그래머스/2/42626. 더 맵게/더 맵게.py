import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)   # 리스트를 힙으로 변환 O(N)
    
    while scoville[0] < K:
        if len(scoville) < 2:
            return -1          # 섞을 수 없으면 -1
        tmp1 = heapq.heappop(scoville)
        tmp2 = heapq.heappop(scoville)
        heapq.heappush(scoville, tmp1 + tmp2 * 2)
        answer += 1
    
    return answer