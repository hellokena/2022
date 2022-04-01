# 럭키스트레이트
def solution(n):
    n = list(map(int, list(n)))
    if sum(n[:len(n)//2]) == sum(n[len(n)//2:]): print("LUCKY")
    else: print("READY")

n = input()
solution(n)
