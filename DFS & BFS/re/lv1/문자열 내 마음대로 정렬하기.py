def solution(strings, n):
    # 첫번째 인자는 인덱스 기준
    # 두번째 인자는 사전순기준
    # 그냥 인덱스 기준만 해버리면 들어온 순서대로 정렬해버림
    strings.sort(key=lambda x:(x[n],x))
    return strings
