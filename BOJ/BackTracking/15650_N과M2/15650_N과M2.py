import sys
input = sys.stdin.readline()

N, M = map(int, input.split())
visited = [False] * (N+1)
answer = []

def dfs(n):
    # 종료 조건
    if len(answer) == M:
        print(' '.join(map(str, answer)))
        return

    for i in range(n, N+1): # 오름차순(이전 선택한 수보다 작은 수는 for문을 돌지 않음)
        # 중복 제거
        if visited[i]:
            continue

        visited[i] = True
        answer.append(i)
        dfs(i+1)
        answer.pop()
        visited[i] = False


dfs(1)