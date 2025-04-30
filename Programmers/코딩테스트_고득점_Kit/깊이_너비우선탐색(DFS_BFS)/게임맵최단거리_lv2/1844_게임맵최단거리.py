from collections import deque

def solution(maps):
    N, M = len(maps), len(maps[0])
    
    answer = bfs(0, 0, N, M, maps) # 시작 위치 x, y, 끝나는 위치 N, M, maps
    
    return answer

def bfs(x, y, N, M, maps):
    visited =  [ [False] * M for i in range(N) ] 
    visited[x][y] = True # 처음 방문한 지점 방문 처리
    
    queue = deque([(x, y, 1)]) # 처음 지점 x, y, dist(=0)으로 queue 초기화
    
    # 방향 벡터 
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    
    # bfs
    # queue가 빌때까지
    while queue:
        cx, cy, d = queue.popleft()
        
        # 종료 조건(끝나는 지점에 도달하면 현재 거리(d) return)
        if cx == N-1 and cy == M-1:
            return d
        
        # 상하좌우 이동
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            
            # 범위 체크 & 벽 체크
            if (0 <= nx < N and 0 <= ny < M) and maps[nx][ny] == 1:
                # 방문 여부 체크
                if not visited[nx][ny]:
                    # 방문 & queue append & 거리 업데이트
                    visited[nx][ny] = True
                    queue.append((nx, ny, d+1))
                    
    # queue가 빌때까지 종료 지점 도달 못했으면 -1 return
    return -1
        
    
    
    
    