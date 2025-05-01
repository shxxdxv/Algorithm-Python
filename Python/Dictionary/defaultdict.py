from collections import defaultdict

# 선언(int를 default_factory로 사용)
count_dict = defaultdict(int)

# 없는 키에 접근 -> 자동으로 0 생성
count_dict['Apple'] += 1
count_dict['Banana'] += 1
count_dict['Apple'] += 1

print(list(count_dict.items()))
print(count_dict['Grape']) # 존재하지 않는 key에 대해 Grape key 생성하고, value 자동으로 생성하여 return 

# list를 default_factory로 사용
group_dict = defaultdict(list)

# 자동으로 list 생성 
group_dict['fruits'].append('Apple')
group_dict['vegetables'].append('Carrot')
group_dict['fruits'].append('Banana')

print(list(group_dict.items()))
print(group_dict.get('snacks')) # None(list로 감싸면 error) : 변화없음
print(group_dict['snacks']) # [] : 데이터 추가 됨 


# 선언할 때 default_factory 지정 안하면
df_dict = defaultdict()
df_dict['any'] += 1 # error 발생 
print(df_dict)