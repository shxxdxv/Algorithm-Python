# visited, answer 배열 필요 -> visited 빈 배열로 설정하면 ( 9, 9 ) 케이스에서 걸림
# check 변수 사용 -> 이전에 선택한 숫자 기억
#   sort() 해놨기 때문에, 이전에 선택한 숫자만 기억해도 된다!   
#   check가 함수 안에 있는 이유는, DFS에서 각각 독립적으로 중복을 체크하기 위함!

N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

answer = []
visited = [False] * N

def dfs():
    if len(answer) == M:
        print(' '.join(map(str, answer)))
        return
    
    # 왜 check가 여기서 0으로 초기화? -> 종료조건을 만족하고 끝난 경우 check가 다시 0으로 초기화되지 않기 때문에 이전 선택 숫자를 기억한다...!
    # 종료조건 만족 -> check는 이전 선택한 숫자 -> 다시 for문으로 돌아감 
    check = 0
    
    for i in range(N):
        if not visited[i] and check != arr[i]:
            visited[i] = True
            answer.append(arr[i])
            check = arr[i]
            dfs()
            answer.pop()
            visited[i] = False

dfs()
