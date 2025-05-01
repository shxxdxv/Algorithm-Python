import bisect
# 정렬된 리스트
data = [1, 3, 3, 5, 8, 12, 15]

# 6이 삽입될 위치 찾기
insert_pos_6 = bisect.bisect_left(data, 6)
print(insert_pos_6)

# 3이 삽입될 위치 찾기 (기존 3들의 오른쪽)
insert_pos_3_right = bisect.bisect_right(data, 3)

# 5를 삽입
bisect.insort_left(data, 5)

# 3을 삽입
bisect.insort_left(data, 3)