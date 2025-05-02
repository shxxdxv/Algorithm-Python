from collections import defaultdict
def solution(n, wires):
    answer = 100
    
    '''
    전력망 끊기 : wire에서 하나씩 제외하고 연결 dict 만들기 
    덩어리세기 : 끊은 지점부터 dfs 각각 해서 차이 구하면됨 
    절댓값 업데이트 
    '''
    
    def dfs(start, top_dict, visited):
        
        visited[start] = True
        cnt = 1
        
        # 현재 노드와 연결된 노드 확인 
        for wire in top_dict[start]:
            # 방문 안한 노드라면 
            if not visited[wire]:
                
                cnt += dfs(wire, top_dict, visited)
               
        return cnt 
    
    # 하나씩 wire 끊기
    for i in range(len(wires)):
        
        # 끊어진 wire 제외하고 그래프 만들기 
        top_dict = defaultdict(list)
        for idx, wire in enumerate(wires):
            if i != idx : 
                top_dict[wire[0]].append(wire[1])
                top_dict[wire[1]].append(wire[0])
        
        # 현재 전선을 끊으면 두 덩어리로 나누어지기 때문에
        # 두 덩어리의 노드 수를 세기 위한 visited 리스트를 초기화하고
        # 끊어진 전선 각각을 시작점으로 하여 덩어리 카운트
        visited = [False] * (n+1)
        component1_size = dfs(wires[i][0],top_dict, visited)
        component2_size = dfs(wires[i][1],top_dict, visited)
        
        answer = min(answer, abs(component1_size - component2_size))
        
    
    return answer