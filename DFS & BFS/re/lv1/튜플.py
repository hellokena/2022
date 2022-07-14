from collections import Counter
def solution(s):
    answer = []
    s = s.replace('{','')
    s = s.replace('}','')
    temp = list(map(int, s.split(',')))
    temp_count = Counter(temp).most_common()
    #temp_count = list(reversed(Counter(temp).most_common()))
    for item in temp_count:
        answer.append(item[0])
    return answer
