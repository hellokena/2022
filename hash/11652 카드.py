import sys
from collections import defaultdict
input = sys.stdin.readline

def solution(n,nums):
    dict = defaultdict(int)
    for num in nums:
        dict[num] += 1
    answer = sorted(dict.items(),key=lambda x:(-x[1],x[0]))
    print(answer[0][0])

n = int(input())
nums = []
for _ in range(n):
    nums.append(int(input()))
solution(n,nums)
