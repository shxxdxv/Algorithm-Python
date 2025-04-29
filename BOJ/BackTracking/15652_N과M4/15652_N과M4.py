import sys
input = sys.stdin.readline()

N, M = map(int, input.split())
answer = []

def dfs(n):
    if len(answer) == M:
        print(' '.join(map(str, answer)))
        return
    
    for i in range(n,  N+1):
        answer.append(i)
        dfs(i)
        answer.pop()

dfs(1)