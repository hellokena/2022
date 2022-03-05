def solution(word):
    cnt = [-1]*26
    for i in range(26):
        # A: 65 a : 97
        if word.count(chr(97+i)):
            cnt[i] = word.index(chr(97+i))
        else: cnt[i] = -1
    #for c in cnt:
        #print(c, end=' ')
    print(' '.join(map(str, cnt)))

word = input()
solution(word)

-----------------------------------------

def solution(word):
    for i in range(97, 97+26):
        print(word.find(chr(i)), end = ' ')

word = input()
solution(word)


