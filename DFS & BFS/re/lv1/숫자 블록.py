# i가 소수일 경우 1을 넣어준다
# 1은 0이다
# 도로 길이는 1,000,000,000이지만 
# 들어가는 수의 최댓값(블록 번호) 10,000,000이므로 10,000,000을 안넘어야만 append 가능
import math
def solution(begin, end):
    answer = []
    for i in range(begin,end+1): # 블록의 번호
        if i == 1: 
            answer.append(0)
            continue
        for j in range(2,int(math.sqrt(i))+1):
            if i%j == 0 and i//j<=10000000: # 큰 경우 어차피 안넣어도됨, 그까지 돌지도 않음(효율성 관련)
                # 나누어지는 수(약수) 있으면 append(1 제외) 최대 약수 구해야 하니까(반대수)
                answer.append(i//j)
                break
        else: answer.append(1)
    return answer
            
            
                
        
