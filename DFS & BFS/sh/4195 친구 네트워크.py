from collections import defaultdict
from collections import deque
import sys
input = sys.stdin.readline

def find(target,parent):
    # 자신이 부모노드인 경우 자신을 리턴
    if parent[target] == target: return target
    # 아닌 경우 재귀를 통해 부모 노드를 계속해서 찾음
    parent[target] = find(parent[target],parent)
    return parent[target]

def union(x,y,parent,cnt):
    x = find(x,parent)
    y = find(y,parent)
    if x!=y:
        parent[y] = x # y의 부모 노드를 x의 부모 노드로 바꿔줌
        cnt[x] += cnt[y] # y를 탐색한 횟수도 x에 더해줌
    #print(cnt[x])

def solution(r,temp):
    parent = {}
    cnt = {}
    for a,b in temp:
        if a not in parent:
            parent[a] = a
            cnt[a] = 1 # 처음 보는 친구니까 탐색 횟수 초기화
        if b not in parent:
            parent[b] = b
            cnt[b] = 1 # 처음 보는 친구니까 탐색 횟수 초기화
        union(a,b,parent,cnt)
        print(cnt[find(a,parent)])
t = int(input())
for _ in range(t):
    r = int(input())
    temp = []
    for _ in range(r):
        temp.append(input().split())
    solution(r,temp)
