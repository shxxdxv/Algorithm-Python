from itertools import permutations

def solution(numbers):
    answer = 0
    
    # 숫자 리스트
    num_list = list(numbers)
    
    permutaion_list = set()
    for i in range(1, len(num_list)+1):
        
        nPr = list(permutations(num_list,i))
        
        for p in nPr:
            pnum = int(''.join(map(str, p)))
            
            if pnum > 1 and pnum not in permutaion_list:
                permutaion_list.add(pnum)
    
    # 소수 판별 
    for num in permutaion_list:
        cnt = 0
        for n in range(2, num):
            if num % n == 0:
                cnt += 1
            if cnt > 0: break
        if cnt == 0 : answer += 1
            
        
    return answer


## Sol 2 
'''
모든 순열 구한 후, 에라토스테네스 체를 이용해 숫자 제거
'''

from itertools import permutations
def solution(n):
    a = set()
    for i in range(len(n)):
        a |= set(map(int, map("".join, permutations(list(n), i + 1))))
    a -= set(range(0, 2))
    for i in range(2, int(max(a) ** 0.5) + 1):
        a -= set(range(i * 2, max(a) + 1, i))
    return len(a)