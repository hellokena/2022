import itertools
def solution(numbers):
    answer = []
    temp = list(itertools.combinations(numbers, 2))
    for i in temp:
        answer.append(sum(i))
    answer = list(set(answer))
    answer.sort()
    return answer

def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            answer.append(numbers[i]+numbers[j])        
    return sorted(list(set(answer)))
