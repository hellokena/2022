def solution(wordl,senl,word,sen):
    wordstate = [0]*52
    senstate = [0]*52
    for i in range(wordl): # 대문자 65 소문자 97
        if word[i].isupper(): # 대문자
            wordstate[ord(word[i])-ord('A')+26] += 1
        else:
            wordstate[ord(word[i])-ord('a')] += 1
    start,length,count = 0,0,0
    for i in range(senl):
        if sen[i].isupper():
            senstate[ord(sen[i])-ord('A')+26] += 1
        else:
            senstate[ord(sen[i])-ord('a')] += 1
        length += 1 # 길이가 4개가 되면
        # 1~4 다음에는 2~5 그래서 처음꺼 빼줘야 함
        if length == wordl:
            if wordstate == senstate: count += 1 # 배열이 같으면
            if sen[start].isupper(): # 슬라이딩 윈도우
                senstate[ord(sen[start])-ord('A')+26] -= 1
            else:
                senstate[ord(sen[start])-ord('a')] -= 1
            start += 1 # 시작부분을 점차적으로 빼주기 위해서
            length -= 1 # 우선 시작부분을 뺴줬으니까 길이도 빼줌, 어차피 나중에 더해줌
    print(count)
 # 슬라이딩 윈도우

findl,mayal = map(int,input().split())
find = input()
maya = input()
solution(findl,mayal,find,maya)
