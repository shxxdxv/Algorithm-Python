def solution(name):
    
    # 조이 스틱 조작 횟수
    answer = 0
    
    # 기본 최소 좌우 이동 횟수 : 전체 길이 - 1
    min_move = len(name) - 1
    
    for i, c in enumerate(name):
        ## 상하 조작
        # 해당 알파벳 변경
        answer += min(ord(c) - ord('A'), ord('Z') - ord(c) + 1)
        
        ## 좌우 조작
        # 해당 알파벳 다음부터 연속된 A 문자열 찾기(좌우 조작)
        next = i + 1
        while next < len(name) and name[next] == 'A':
            next += 1
        
        # 기존, 연속된 A의 왼쪽부터, 연속된 A의 오른쪽부터 방식 비교 및 갱신
        min_move = min([min_move, 2 * i + len(name) - next, i + 2 * (len(name)- next)])
        
    # 좌우이동 횟수 추가
    answer += min_move
    return answer
        
        
        
        
        
        