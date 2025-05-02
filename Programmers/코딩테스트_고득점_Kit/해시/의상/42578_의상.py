from collections import defaultdict

def solution(clothes):
    answer = 1
    clothes_dict = defaultdict(int)
    
    for cloth in clothes:
        clothes_dict[cloth[1]] += 1
    
    # 각 종류의 옷을 하나씩 고름(선택하지 않는 경우를 위해 + 1)
    for c in clothes_dict:
        answer *= (clothes_dict[c] + 1)
        
    # 아무것도 안입는 경우 1가지 제외 
    return answer-1
