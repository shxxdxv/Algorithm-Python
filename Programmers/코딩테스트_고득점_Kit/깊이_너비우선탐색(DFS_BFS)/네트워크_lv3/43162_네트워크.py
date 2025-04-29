from collections import deque

def solution(n, computers):
    answer = 0
    visited = [False] * n
    
    for i in range(n):
        if not visited[i]:
            bfs(i, visited, computers)
            answer += 1
    print(answer)
    return answer

def bfs(n, visited, computers):
    queue = deque([n])
    visited[n] = True
    
    while queue:
        c = queue.popleft()
        
        for i in range(n+1, len(computers)):
            if computers[c][i] == 1 and not visited[i]:
                queue.append(i)
                visited[i] = True

solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]])