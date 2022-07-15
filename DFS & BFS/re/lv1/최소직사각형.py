# 명함갯수는 4개가 아니다.. 문제 제대로 읽자
def solution(sizes):
    for size in sizes: # 가로, 세로 구분 없이 짧은 거 앞에
        size.sort()
    w = [size[0] for size in sizes]
    h = [size[1] for size in sizes]
    return max(w) * max(h)
