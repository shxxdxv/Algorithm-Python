def solution(phone_book):
    answer = True
    phone_book.sort()
    dic = {}
    for phone in phone_book:
        dic[phone] = True
        
    for phone in phone_book:
        
        for n in range(1, len(phone)):
            prefix = phone[:n]
            if prefix in dic.keys():
                return False
    
    return answer