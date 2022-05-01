def solution(n,temp):
    temp.sort(key=lambda x:x[0])
    for age,name in temp:
        print(int(age), name)

n = int(input())
temp = []
for _ in range(n):
    age, name = input().split()
    temp.append([int(age),name])
solution(n,temp)
