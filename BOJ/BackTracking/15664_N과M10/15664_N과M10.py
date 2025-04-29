N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

answer = []
visited = [False] * (N)

def dfs(n):
    if len(answer) == M:
        print(' '.join(map(str, answer)))
        return
    
    check = 0

    for i in range(n, N):
        if not visited[i] and check != arr[i]:
            visited[i] = True
            answer.append(arr[i])
            check = arr[i]
            dfs(i+1)
            answer.pop()
            visited[i] = False
    
    
dfs(0)