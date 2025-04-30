answer = float('INF')

def solution(begin, target, words):

    visited = {begin} # begin 담은 visited set 

    # dfs : 시작단어, 목표 단어, 단어 배열, visited 배열, 변환 횟수 
    dfs(begin, target, words, visited, 0)
    
    # 변환 실패하면 0 return
    if answer == float('INF'):
        return 0
    else :
        return answer


def dfs(begin, target, words, visited, k):
    global answer
    
    # 종료 조건(begin == target)
    if begin == target :
        answer = min(answer, k)
        return 
    
    # 단어 목록 돌면서 변환 가능한 단어 탐색 
    for word in words:

        # 아직 방문 안했으면
        if word not in visited:

            # 변환 가능한지 체크
            diff_cnt = 0
            for b, w in zip(begin, word):
                if b != w : diff_cnt += 1
                if diff_cnt > 1 : break # 다른 알파벳이 1개가 아니면 그냥 바로 탈출
            
            # 변환 가능하면(다른 알파벳이 1개)
            if diff_cnt == 1:
                visited.add(word) # 방문 표시
                dfs(word, target, words, visited, k+1)
                visited.remove(word) # 다른 경로에서도 방문할 수 있도록 remove

                
    