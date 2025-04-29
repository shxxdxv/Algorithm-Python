N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

visited = []
answer = []

def dfs():
    if len(answer) == M:
        print(' '.join(map(str, answer)))
        return
    
    for i in arr:
        if i in visited : continue

        visited.append(i)
        answer.append(i)
        dfs()
        answer.pop()
        visited.pop()

dfs()