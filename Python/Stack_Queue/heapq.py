import heapq

data = [4, 7, 5, 3, 1]

# 리스트를 heap으로 변환
heapq.heapify(data)

# push
# O(log n)
heapq.heappush(data, 10)
heapq.heappush(data, 8)

# pop
# 비어있으면 error
# O(log n)
heapq.heappop(data) # 가장 작은 요소(index 0)


# heappushpop(heap, data)
# item 추가하고(정렬) 가장 작은 요소 pop
# O(log n)
heapq.heappushpop(data, 8)


# replace
# pop 수행 -> push
heapq.heapreplace(data, 2)

# nlargest(n, iterable, key=None)
# 가장 큰 n개의 요소 리스트로 반환(정렬 X)
# O(nlog n)
heapq.nlargest(2, data, key=len)


# nsmallest(n, iterable, key=None)
# 가장 작은 n개의 요소 리스트로 반환(정렬 X)
# O(nlog n)
heapq.nlargest(3, data)