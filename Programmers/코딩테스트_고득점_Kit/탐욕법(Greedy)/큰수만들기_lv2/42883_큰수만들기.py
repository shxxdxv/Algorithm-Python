def solution(number, k):
    # stack :: 수가 차례대로 담김(큰수부터)
    stack = []
    
    for num in number:
        # 제거할 수 k가 남아있고
        # 스택에 값이 있고
        # 스택의 마지막 값이 num보다 작다면
        # 제거 후 제거할 수 k 없데이트
        while (k > 0) and (stack) and (stack[-1] < num):
            stack.pop()
            k -= 1
        # 값 추가
        stack.append(num)
        
    # k가 남아있는 경우
    if k > 0:
        stack = stack[:-k]
    
    return "".join(stack)
        