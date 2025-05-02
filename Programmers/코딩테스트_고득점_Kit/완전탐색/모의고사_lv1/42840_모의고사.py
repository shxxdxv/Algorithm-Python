# 1 : 1 2 3 4 5 -> 5씩 반복 idx : n % 5
# 2 : 2 1 2 3 2 4 2 5 -> 8씩 반복 : n % 8
# 3 : 3 3 1 1 2 2 4 4 5 5 -> 10씩 반복 : n % 10

from collections import defaultdict

def solution(answers):
    answer = []
    count_dict = defaultdict(int)
    
    answer_list = [ [1, 2, 3, 4, 5], [2, 1, 2, 3, 2, 4, 2, 5], [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] ]
    
    for idx, a in enumerate(answers):
        # 1
        if a == answer_list[0][idx%5] :
            count_dict[1] += 1
        # 2
        if a == answer_list[1][idx%8] :
            count_dict[2] += 1
        
        # 3
        if a == answer_list[2][idx%10] :
            count_dict[3] += 1

    max_score = max(count_dict.values())
    for item in count_dict.items():
        if item[1] == max_score:
            answer.append(item[0])
        
    return sorted(answer)




def solution(answers):
    p = [[1, 2, 3, 4, 5],
         [2, 1, 2, 3, 2, 4, 2, 5],
         [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    s = [0] * len(p)

    for q, a in enumerate(answers):
        for i, v in enumerate(p):
            if a == v[q % len(v)]:
                s[i] += 1
    return [i + 1 for i, v in enumerate(s) if v == max(s)]
