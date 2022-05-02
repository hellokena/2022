def solution(n,in_,out):
    answer = 0
    dict = {}
    for i,car in enumerate(in_):
        dict[car] = i # 들어온 순서 기록
    for i in range(n):
        for j in range(i,n):
            # 뒤에꺼부터 확인
            # 현재 차량이 들어간 순서가 뒤에 나오는 차량들의 인덱스보다 큰 경우 있으면 추월
            # 뒤에 차량이 앞차보다 먼저 나오면
            # 인덱스가 크면 뒤에 들어온 거니까
            if dict[out[i]] > dict[out[j]]: # 나오는 차량 순서대로 확인
                answer += 1
                break
    print(answer)


n = int(input())
in_ = []
out = []
for i in range(n):
    in_.append(input())
for i in range(n):
    out.append(input())
solution(n,in_,out)
