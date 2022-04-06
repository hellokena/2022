from collections import defaultdict
def solution(n,book):
    dict = defaultdict(int)
    for b in book:
        dict[b] += 1
    answer = sorted(dict.items(), key=lambda x:(-x[1],x[0]))
    print(answer[0][0])

n = int(input())
book = []
for _ in range(n):
    book.append(input())
solution(n,book)
