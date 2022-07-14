import math
from itertools import combinations
def sosu(num):
    for i in range(2,int(math.sqrt(num))+1):
        if num % i == 0: return False # 소수가 아님
    return True # 소수임

def solution(nums):
    answer = 0
    comb = list(combinations(nums,3))
    for c in comb:
        if sosu(sum(c)):
            answer += 1
    return answer

   
