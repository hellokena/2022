from collections import defaultdict
def solution(genres, plays):
    answer = []
    stream = defaultdict(list)
    # 같은 장르내에서는 plays수가 같을 수 있지만
    # 장르 합은 다른 장르의 합과 다르다
    for g,p in zip(genres, plays):
        stream[g].append(p)
    answer = []
    stream = sorted(stream.items(), key = lambda x:-sum(x[1])) # list
    # 인덱스는 앞에것부터 찾음
    for i,j in stream:
        j.sort(reverse=True)
    for i in range(len(stream)): #장르가 2개 이상 가능
        if len(stream[i][1]) == 1: answer.append(plays.index(stream[i][1][0]))
        else: # 길이가 2이상 (2개 다 넣일 수 있음)
            answer.append(plays.index(stream[i][1][0]))
            plays[plays.index(stream[i][1][0])] = -1
            answer.append(plays.index(stream[i][1][1]))
    return answer
