def solution(files):
    answer = ''
    temp = []
    for file in files:
        temp.append(list(file))
    # transpose
    ttemp = [[0 for row in range(len(temp))] for col in range(len(temp[0]))]
    for i in range(len(temp)): # 행
        for j in range(len(temp[0])): # 열
            ttemp[j][i] = temp[i][j]
    for i in ttemp:
        flag = True # 같다고 가정
        temporary = i[0]
        for j in i:
            if j == temporary: continue
            else: flag = False
        if flag == True:
            answer += temporary
        else: answer += '?'
    print(answer)

n = int(input()) # 파일 이름의 개수
files = [input() for i in range(n)]
solution(files)

# ------

def solution(files):
    answer = ''
    temp = []
    for file in files:
        temp.append(list(file))

    for i in range(len(temp[0])): # 각 문자를 비교해줄 커서
        temporary = None # 기준 문자열 임시 변수
        flag = True # 같다고 가정
        for t in temp:
            if not temporary: # 처음 temporary
                temporary = t[i] # 첫 문자를 temp로 저장 ##
            else:
                if t[i] != temporary: # 다르다면 ##
                    flag = False

        if flag: answer += temporary
        else: answer += '?'

    print(answer)

n = int(input()) # 파일 이름의 개수
files = [input() for i in range(n)]
solution(files)
