# 그리디 # ATM
# 누적합
def solution(n, people):
    answer = 0
    tmp = 0
    people.sort()
    for i in people:
        tmp += i
        answer += tmp
    print(answer)

n = int(input())
people = list(map(int, input().split()))
solution(n, people)
