def solution(people, limit):
    answer = 0
    
    people.sort()
    start, end = 0, len(people) - 1
    
    while(start <= end):
        if start == end:
            answer += 1
            break
        if people[start] + people[end] <= limit:
            start += 1
        
        end -= 1
        
        answer += 1
            
    return answer