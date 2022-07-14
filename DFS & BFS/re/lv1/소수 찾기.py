import math
from itertools import permutations

def prime(num):
    # 0과 1의 경우 판별해주는 알고리즘 로직 필요
    if num in [0,1]: return False
    for i in range(2,int(math.sqrt(num))+1):
        if num % i == 0: return False
    return True

def solution(numbers):
    cnt = 0
    answer = []
    temp = []
    for i in range(1,len(numbers)+1): # 만들 수 있는 모든 경우의 수
        answer.extend(list(permutations(numbers,i)))
    for ans in answer: # 문자열 형식으로 전환
        temp.append(''.join(ans))
    temp = list(set(map(int, temp))) # 숫자 형식으로 전환 후 중복 제거 후 리스트
    for t in temp: # 소수 판별
        if prime(t): cnt += 1  
    return cnt
