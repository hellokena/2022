def solution(lottos, win_nums):
    min_cnt = 0
    max_cnt = 0
    for lotto in lottos:
        if lotto == 0: max_cnt += 1
        elif lotto in win_nums:
            max_cnt += 1
            min_cnt += 1
    return [min(6,7-max_cnt), min(6,7-min_cnt)]

def solution(lottos, win_nums):
    correct = 0
    rank = [6,6,5,4,3,2,1]
    zeros = lottos.count(0)
    for lotto in lottos:
        for win_num in win_nums:
            if lotto == win_num:
                correct += 1 # 맞힌 갯수
    return [rank[correct+zeros],rank[correct]]
