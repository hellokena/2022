def solution(d, budget):
    answer = 0
    num = 0
    d.sort()
    for i in d:
        if answer + i <= budget:
            answer += i
            num += 1
        else: return num # 같거나 커지면
    return num
  
  def solution(d, budget):
    temp = 0
    cnt = 0
    d.sort()
    for i in d:
        temp += i
        if temp > budget:
            break
        cnt += 1
    return cnt
  
  def solution(d, budget):
    temp = 0
    cnt = 0
    d.sort()
    for i in d:
        temp += i
        if temp <= budget:
            cnt += 1
        else: break
    return cnt
  
  def solution(d, budget):
    cnt = 0
    d.sort()
    for i in d:
        budget -= i
        if budget < 0:
            break
        cnt += 1
    return cnt
