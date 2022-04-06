def solution(n,m,sites,findsites):
    sites = dict(sites)
    for findsite in findsites:
        print(sites[findsite])

n,m = map(int, input().split())
sites = []
findsites = []
for _ in range(n):
    sites.append(list(input().split()))
for _ in range(m):
    findsites.append(input())
solution(n,m,sites,findsites)
