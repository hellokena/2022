def solution(n):
    n = list(map(int, str(n)))
    n.sort(reverse=True)
    print(''.join(map(str, n))) # join은 str형만 가능하다

n = int(input())
solution(n)
