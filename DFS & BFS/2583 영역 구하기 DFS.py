#dfs
# 덩어리 세기
import sys
sys.setrecursionlimit(10**5)

def dfs(i,j,m,n,graph): # 갈 수 없는 곳을 탐색한다
    global answer
    answer += 1
    graph[i][j] = 1 # 갈 수 있는 곳으로 처리한다
    # 상하좌우 방향벡터
    dh = [-1, 1, 0, 0]
    dw = [0, 0, -1, 1]
    for r in range(4):
        nh = i + dh[r]
        nw = j + dw[r]
        if 0<=nh<m and 0<=nw<n and graph[nh][nw] == 0:
            dfs(nh,nw,m,n,graph)
    return answer

def solution(m,n,k,graph): # 갈 수 없는 곳을 탐색한다
    #total = 0
    temp = []
    for i in range(m): # 세로
        for j in range(n): # 가로
            if graph[i][j] == 0:
                global answer
                answer = 0
                temp.append(dfs(i,j,m,n,graph))
                #dfs(i,j,m,n,graph) # return answer 없을 때
                #temp.append(answer)
                #total += 1

    #print(total)
    print(len(temp))
    print(' '.join(map(str, sorted(temp))))

m,n,k = map(int, input().split()) # height, width, 직사각형 갯수
graph = [[0]*n for _ in range(m)]
for _ in range(k):
    sh,sw,eh,ew = map(int, input().split())
    for i in range(sw, ew): # 세로
        for j in range(sh, eh): # 가로
            graph[i][j] = 1 # 갈 수 있는 곳
solution(m,n,k,graph)
