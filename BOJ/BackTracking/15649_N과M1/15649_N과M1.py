# s3 / sol / 160ms

import sys
input = sys.stdin.readline()

N, M = map(int, input.split())
visited = [False] * (N+1) # 중복 제거
answer = []

def dfs():
    # 종료 조건
    if len(answer) == M:
        print(' '.join(map(str, answer)))

    for i in range(1, N+1):
        # 이미 선택 되었으면 (visited == True) 다음 숫자로 넘어감
        if visited[i] : 
            continue

        # 선택
        visited[i] = True
        answer.append(i)
        dfs()
        # 다음 숫자에 영향 주지 않도록 answer에서 제거
        answer.pop()
        visited[i] = False

dfs()