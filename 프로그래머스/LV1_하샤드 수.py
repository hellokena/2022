def solution(x):
    answer = True
    temp = list(map(int, str(x)))
    if x%sum(temp) == 0: return True
    else: return False
