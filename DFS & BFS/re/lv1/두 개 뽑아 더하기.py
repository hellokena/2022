from itertools import combinations
def solution(numbers):
    answer = []
    comb = list(combinations(numbers,2))
    for i,j in comb:
        if i+j not in answer:
            answer.append(i+j)
    answer.sort() 
    return answer
  
  def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        for j in range(i+1,len(numbers)):
            if numbers[i]+numbers[j] not in answer: 
                answer.append(numbers[i]+numbers[j])
    answer.sort()
    return answer # set 써도 무관...
  
 ## 겁나 효율적
def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        for j in range(i+1,len(numbers)):
            answer.append(numbers[i]+numbers[j])
    return sorted(set(answer)) # set 써도 무관...
