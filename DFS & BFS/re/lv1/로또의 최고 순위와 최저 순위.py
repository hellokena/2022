def solution(lottos, win_nums):
    min_cnt = 0
    max_cnt = 0
    for lotto in lottos:
        if lotto == 0: max_cnt += 1
        elif lotto in win_nums:
            max_cnt += 1
            min_cnt += 1
    return [min(6,7-max_cnt), min(6,7-min_cnt)]
