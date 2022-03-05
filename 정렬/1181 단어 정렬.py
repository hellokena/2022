def solution(n, words):
    words = list(set(words)) # 중복제거
    words.sort() # 조건2
    words.sort(key=lambda x:len(x)) # 조건1
    for word in words:
        print(word)

n = int(input())
words = []
for _ in range(n):
    words.append(input())
solution(n, words)
