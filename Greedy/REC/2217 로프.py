# 그리디 # 로프
# 각 로프의 값은 해당 ㄹ프가 버틸 수 있는 최대 중량

def solution(n, rope):
    rope.sort(reverse=True)
    for i in range(n):
        rope[i] = rope[i] * (i+1)
    print(max(rope))

n = int(input())
rope = []
for _ in range(n):
    rope.append(int(input()))
solution(n,rope)
