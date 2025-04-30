
def solution(tickets):
    answer = [] # 방문 경로를 담는 배열(여러개가 될 수 있음(tc:2))
    visited = [False] * len(tickets)
    
    def dfs(end, path):
        # 종료 조건
        # 모든 항공권 다 쓰면 answer에 경로 추가 
        if len(path) == len(tickets) + 1:
           
            answer.append(path[:]) # 값 복사 안하고 그냥 path만 넣으면 밑에서 path를 조작하기 때문에 answer에서의 path 값도 변한다!
            return
        
        # recursive
        # end(직전에 간 공항) == 시작 공항이면 경로 추가 가능
        for idx, ticket in enumerate(tickets):
            # 방문한 적 없고, end == ticket[0](시작공항)이면
            if not visited[idx] and (end == ticket[0]):
                visited[idx] = True
                path.append(ticket[1])
                dfs(ticket[1], path )
                visited[idx] = False
                path.pop()
    
    dfs("ICN", ["ICN"])
    answer.sort()
    
    
    return answer[0]