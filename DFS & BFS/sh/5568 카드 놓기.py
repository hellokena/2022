from itertools import permutations
def solution(n,k,cards):
    answer = set()
    for i in permutations(cards,k):
        temp = ''.join(map(str,i))
        answer.add(temp)
    print(len(answer))

cards = []
n = int(input())
k = int(input())
for _ in range(n):
    cards.append(int(input()))
solution(n,k,cards)
