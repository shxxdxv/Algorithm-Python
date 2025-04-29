N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

answer = []

def dfs():
    # 종료 조건
    if len(answer) == M:
        print(' '.join(map(str, answer)))
        return
    
    # 중복 방지를 위한 check 변수
    check = 0

    for i in range(N):
        if check != arr[i]:
            answer.append(arr[i])
            check = arr[i]
            dfs()
            answer.pop()

dfs()
