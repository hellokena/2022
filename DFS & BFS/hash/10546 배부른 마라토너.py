import sys
input = sys.stdin.readline

def solution(n,participant,completion):
    participant.sort()
    completion.sort()
    for p,c in zip(participant,completion):
        if p!=c:
            print(p)
            return p
    print(participant[-1])
    return participant[-1]

n = int(input())
participant = []
completion = []
for _ in range(n):
    participant.append(input())
for _ in range(n-1):
    completion.append(input())
solution(n,participant,completion)
