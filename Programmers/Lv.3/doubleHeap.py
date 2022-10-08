# 프로그래머스 이중우선순위큐
# start time 07:36      end time: 07:51     ** 검색 도움 받음
import heapq
from heapq import heappush, heappop
def solution(operations):

    heap = []
    for oper in operations:
        m = oper[:1]
        n = int(oper[2:])
        if m == 'I':
            heapq.heappush(heap, n)
        elif len(heap) > 0:
            if n > 0:
                heap.pop(heap.index(heapq.nlargest(1,heap)[0]))
            else:
                heapq.heappop(heap)
    if len(heap) == 0:
        return [0,0]
    return [heapq.nlargest(1,heap)[0], heap[0]]
