# 덮어쓰기
import sys
input = sys.stdin.readline

def solution(k,l,students):
    dict = {}
    for i,s in enumerate(students):
        dict[s] = i # 덮어쓰기
    dict = sorted(dict.items(),key=lambda x:x[1])
    if k > len(dict): # 수강신청 인원이 적을 경우 초기화
       k = len(dict)
    for i in range(k):
       print(dict[i][0])

k,l = map(int, input().split())
students = []
for _ in range(l):
    students.append(input().rstrip())
solution(k,l,students)
