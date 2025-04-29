N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

answer = []

def dfs():
    if len(answer) == M:
        print(' '.join(map(str, answer)))
        return
    

    for i in arr:
        answer.append(i)
        dfs()
        answer.pop()

dfs()