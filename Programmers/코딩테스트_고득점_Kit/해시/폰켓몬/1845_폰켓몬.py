# 시간초과
from itertools import combinations
def solution(nums):
    # 최대값( 중복을 제거한 조합의 길이 목록 )
    return max([ len(set(i)) for i in list(combinations(nums, int(len(nums)/2)))])