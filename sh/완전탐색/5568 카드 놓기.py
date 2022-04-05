# silver4 5568 카드 놓기
# 입력값 범위가 작다
# permutation을 사용해도 시간초과가 나지 않을 거라고 생각함

from itertools import permutations
def solution(n,k,nums):
    s = [] # set
    temp = map(list, permutations(nums,k))
    #temp = list(permutations(nums,k))
    for t in temp: # 숫자가 int가 아닌 str형이라면 바로 temp에 바로 permutations(num,k) 대입 가능
        s.append("".join(map(str,t)))
    s = set(s)
    print(len(s))

n = int(input())
k = int(input())
nums = []
for _ in range(n):
    nums.append(int(input()))
solution(n,k,nums)

# ------------------------ㄹ

# silver4 5568 카드 놓기
# 입력값 범위가 작다
# permutation을 사용해도 시간초과가 나지 않을 거라고 생각함

from itertools import permutations
def solution(n,k,nums):
    s = set() # set
    for t in permutations(nums,k):
        s.add("".join(map(str,t))) # list 안에 있는 int 형태 원소들을 str 형태로 변환
    print(len(s))

n = int(input())
k = int(input())
nums = []
for _ in range(n):
    nums.append(int(input()))
solution(n,k,nums)
