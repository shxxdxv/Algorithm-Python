answer = -1
def solution(k, dungeons):
    
    global answer
    
    def dfs(n, visited, k, cnt):        
        global answer
        answer = max(answer, cnt)
        
        # for문 끝까지 돌면 알아서 멈추기 때문에 종료조건 필요 없음 
        # for문을 모두 선회하고, 방문할 수 있는 던전이 더이상 없을 때 재귀 호출은 일어나지 않기 때문에 dfs 함수 실행이 종료 됨 
        for idx, dungeon in enumerate(dungeons):
            if not visited[idx]:
                if dungeon[0] <= k:
                    visited[idx] = True
                    dfs(n+1, visited, k - dungeon[1], cnt + 1)
                    visited[idx] = False
                
    visited = [False] * len(dungeons)
    dfs(0, visited, k, 0)
    return answer