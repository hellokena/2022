def solution(s):
    cnt = 0
    zeros = 0
    while s != '1':
        zeros += s.count('0')
        s = s.replace('0','') # 모든 0 제거
        s = str(bin(len(s))[2:])
        cnt += 1
    return [cnt,zeros]
        
    
 
