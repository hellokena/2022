# dfs
cnt = 0

def dfs(i,j):
    global cnt
    cnt += 1
    graph[i][j] = 0 # 방문처리
    # 상하좌우 방향벡터
    dh = [-1, 1, 0, 0]
    dw = [0, 0, -1, 1]
    for x in range(4):
        nexth = i + dh[x]
        nextw = j + dw[x]
        if 0 <= nexth < n and 0 <= nextw < n and graph[nexth][nextw] == 1:
            #cnt += 1
            dfs(nexth, nextw)

def solution(n):
    #total = 0
    global cnt
    result = []
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 1:
                #cnt = 1
                cnt = 0 # 단지내 집 갯수
                dfs(i,j)
                result.append(cnt)
                #total += 1
    #print(total)
    print(len(result))
    for k in sorted(result):
        print(k)

n = int(input()) # 지도 크기
graph = []
for _ in range(n):
    graph.append(list(map(int, input())))
solution(n)
