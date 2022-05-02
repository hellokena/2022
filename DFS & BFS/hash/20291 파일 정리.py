import sys
from collections import defaultdict
input = sys.stdin.readline
def solution(n,files):
    dict = defaultdict(int)
    for file in files:
        front,rear = file.split('.')
        dict[rear] += 1
    dict = sorted(dict.items())
    for i in dict:
        print(i[0], i[1])

n = int(input())
files = []
for _ in range(n):
    files.append(input().rstrip())
solution(n,files)
