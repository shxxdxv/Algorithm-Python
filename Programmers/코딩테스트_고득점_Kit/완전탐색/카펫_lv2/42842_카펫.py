def solution(brown, yellow):
    answer = []
    '''
    yellow를 한줄씩 늘리자
    '''
    y_h =  1
    while True:
        y_w = yellow / y_h
        if 2 * (y_w + y_h) + 4 == brown :
            answer = [y_w + 2, y_h + 2 ]
            break
        
        elif 2 * (y_w + y_h) + 4 > brown :
            y_h += 1
    return answer


## Sol 2 : for문으로 하나씩 증가하면서 나누어 떨어지면 brown과 비교
def solution(brown, red):
    for i in range(1, int(red**(1/2))+1):
        if red % i == 0:
            if 2*(i + red//i) == brown-4:
                return [red//i+2, i+2]