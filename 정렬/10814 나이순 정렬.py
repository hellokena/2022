def solution(n, people):
    people.sort(key=lambda x:x[0]) # 그냥 sort 쓸때랑 다름
    for age, person in people:
        print(age, person)

n = int(input())
people = []
for _ in range(n):
    age, name = input().split()
    people.append([int(age), name])
solution(n, people)
