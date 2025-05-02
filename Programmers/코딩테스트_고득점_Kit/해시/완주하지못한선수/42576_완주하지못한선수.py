def solution(participant, completion):
    answer = ''
    participant.sort()
    completion.sort()

    
    for i in range(len(completion)):
        if participant[i] != completion[i]:
            answer = participant[i]
            break
    if answer == '':
        answer = participant[-1]
    return answer



# sol 2 : 객체는 값 빼기 가능
import collections

def solution2(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]


# sol 3 : hash 사용 
def solution3(participant, completion):
    answer = ''
    temp = 0
    dic = {}
    for part in participant:
        # 딕셔너리에 해시 값을 키로, 참가자 이름을 값으로 저장합니다.
        # 이렇게 하면 나중에 해시 값만으로 참가자 이름을 찾을 수 있습니다.
        dic[hash(part)] = part
        temp += int(hash(part))
    for com in completion:
        temp -= hash(com)


    # 3. 완주하지 못한 선수 찾기
    # 참가자들의 해시 총합(temp)에서 완주자들의 해시 총합을 빼면,
    # 완주하지 못한 단 한 명의 참가자의 해시 값만 남게 됩니다.
    # 그 이유는 완주한 선수들의 해시 값은 더해졌다가 다시 빼지면서 상쇄되기 때문입니다.
    # 따라서 temp 변수에는 완주하지 못한 선수의 해시 값이 남아 있습니다.
    answer = dic[temp]

    return answer