def solution(x):
    temp = list(str(x))
    temp = list(map(int,temp))
    if x%sum(temp) == 0: return True
    else: return False
    
