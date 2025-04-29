# for문 범위 주의
# 중복 허용이므로 visited 안씀
# 대신 같은 수열 여러번 안되니까 check 변수 사용


N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

answer = []

def dfs(n):
    if len(answer) == M:
        print(' '.join(map(str, answer)))
        return
    
    check = 0

    for i in range(n, N):
        if check != arr[i]:
            answer.append(arr[i])
            check = arr[i]
            dfs(i)
            answer.pop()
    
    
dfs(0)