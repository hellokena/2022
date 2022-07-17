import math
def solution(n):
    answer = set()
    if n in [0,1]: return n
    for i in range(2,int(math.sqrt(n))+1):
        if n % i == 0:
            answer.add(i)
            answer.add(n//i)
    return sum(answer) + 1 + n
