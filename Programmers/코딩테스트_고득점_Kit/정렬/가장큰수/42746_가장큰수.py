def solution(numbers):
    answer = 0
    numbers.sort(key = lambda x : str(x)*3, reverse=True)
    
    
    answer = ''.join(map(str, numbers))
    if sum(numbers) == 0:
        answer = 0
    return str(answer)