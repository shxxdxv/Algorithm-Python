def solution(n, lost, reserve):
    answer = 0
    
    # 모두 다 있다고 가정 
    clothes = [1] * (n+2)
    clothes[0], clothes[n+1] = -1, -1
    
    # 잃어버린 애들은 하나 빼기
    for i in lost:
        clothes[i] -= 1
    # 하나 더 있는 애들은 하나 추가
    for i in reserve:
        clothes[i] += 1
    
    # 앞뒤로 없는 애들한테 빌려주기
    for i in range(1, n+1):
        # 여벌 옷 있으면 
        if clothes[i] == 2:
            if clothes[i-1] == 0:
                clothes[i] -= 1
                clothes[i-1] += 1
            elif clothes[i+1] == 0:
                clothes[i] -= 1
                clothes[i+1] += 1
    
    for c in clothes:
        if c > 0:
            answer += 1
            
        
    return answer