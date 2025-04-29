N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

visited = [] 
answer = []

def dfs(n):
    if len(answer) == M:
        print(' '.join(map(str, answer)))
        return
    
    for i in range(n, N):
        if arr[i] in visited:
            continue
        visited.append(arr[i])
        answer.append(arr[i])
        dfs(i)
        answer.pop()
        visited.pop()

dfs(0)