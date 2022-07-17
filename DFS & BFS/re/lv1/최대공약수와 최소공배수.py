import math
def solution(n, m):
    return [(math.gcd(n,m)),(n*m)//math.gcd(n,m)] # 최소공약수, 최대공배수
    
