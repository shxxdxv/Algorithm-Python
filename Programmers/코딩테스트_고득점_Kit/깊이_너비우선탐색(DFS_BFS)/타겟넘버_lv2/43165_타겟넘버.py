# 전역 변수 선언 
answer = 0

def solution(numbers, target):

    dfs(0, 0, numbers, target)
    return answer

def dfs(k, s, numbers, target):
    # global 키워드로 이 변수가 전역 변수임을 명시 
    global answer

    # 종료 조건 
    if k == len(numbers):
        if s == target:
            answer += 1
        return

    dfs(k+1, s + numbers[k], numbers, target)
    dfs(k+1, s - numbers[k], numbers, target)

