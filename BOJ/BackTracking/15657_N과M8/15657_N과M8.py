# 오름차순으로 정렬해놓고, 중복 허용되게 고르면 알아서 같은 수열 여러번 출력 안되게 됨 

N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

answer = []

def dfs(n):
    if len(answer) == M:
        print(' '.join(map(str, answer)))
        return
    
    for i in range(n, N):
        answer.append(arr[i])
        dfs(i)
        answer.pop()
dfs(0)
