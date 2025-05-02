def solution(array, commands):
    answer = []
    
    for command in commands:
        temp = sorted(array[command[0]-1:command[1]])
        print(temp)
        answer.append(temp[command[2]-1])
    return answer