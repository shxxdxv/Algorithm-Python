import heapq

def solution(ability, number):
    queue = []

    for a in ability:
        heapq.heappush(queue,a) # 자동 정렬

    for n in range(number):
        x = heapq.heappop(queue)
        y = heapq.heappop(queue)
        x_y = x+y
        heapq.heappush(queue,x_y)
        heapq.heappush(queue,x_y)

    answer = sum(queue)
    print(heapq.heappop())
    return answer