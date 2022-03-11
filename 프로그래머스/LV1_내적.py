def solution(a, b):
    answer = 0
    for i,j in zip(a,b):
        answer += i * j
    return answer
  
  def solution(a, b):
    answer = 0
    for i in range(len(a)):
        for j in range(len(b)):
            if i == j:
                answer += a[i]*b[j]
    return answer
  
  def solution(a, b):
    answer = 0
    for i in range(len(a)):
        answer += a[i] * b[i]
    return answer
