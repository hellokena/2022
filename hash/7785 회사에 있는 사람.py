def solution(n,record):
    dict = {}
    for name,rec in record:
        dict[name] = rec # 덮어쓰기
    dict = sorted(dict.items(), reverse=True) # 이름 역순 정렬
    for d in dict:
        if d[1] == "enter":
            print(d[0])

n = int(input())
record = []
for _ in range(n):
    record.append(list(input().split()))
solution(n,record)
