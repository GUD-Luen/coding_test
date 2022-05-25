import heapq


def solution(scoville, K):
    answer = 0
    scoville_heap = scoville
    heapq.heapify(scoville_heap)
    while scoville_heap[0] < K and len(scoville_heap) > 1:
        a = heapq.heappop(scoville_heap)
        b = heapq.heappop(scoville_heap)
        heapq.heappush(scoville_heap, a + 2 * b)
        answer += 1
    if scoville_heap[0] < K:
        return -1
    return answer