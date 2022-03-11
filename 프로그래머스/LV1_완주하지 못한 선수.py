def solution(participant, completion):
    participant.sort()
    completion.sort()
    for i in range(len(completion)):
        if participant[i] != completion[i]:
            return participant[i]
    return participant[-1]
  
  def solution(participant, completion):
    participant.sort()
    completion.sort()
    for p, c in zip(participant, completion):
        if p != c:
            return p
    else: return participant[-1]    
    
    
from collections import Counter
def solution(participant, completion):
    temp = list(Counter(participant) - Counter(completion))
    return ''.join(temp)
