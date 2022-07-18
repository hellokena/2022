def solution(s):
    answer = []
    if len(s) == 1: return 1 # 길이가 1개일 경우 압축이고 뭐고 1 리턴
    for i in range(1,(len(s)//2)+1): # 압축할 기준 문자열 갯수
        compaction = '' # 압축 문자열 저장할 변수
        criteria = s[:i] # 기준이 될 문자열
        cnt = 1 # 현재 문자열 반복 횟수
        for j in range(i,len(s),i): # 압축할 기준 문자열 갯수로 돔
            if s[j:i+j] == criteria: # 기준 문자열과 같으면
                cnt += 1
            else: # 기준 문자열과 다른 경우
                if cnt > 1: # 같은 문자열을 2회 이상 돈 경우 압축
                    compaction = compaction + str(cnt) + criteria
                else: # 2회 이상 돌지 못했을 경우 압축 불가 # 그냥 기준 문자열 더하기
                    compaction += criteria
                criteria = s[j:j+i] # 초기화 # 다음꺼 돌아야 하니까
                cnt = 1 # 초기화
        if cnt > 1: # 기준 문자열과 계속 같은 경우 위의 추가 로직 돌지 못하므로 마지막으로 한번 더
            compaction = compaction + str(cnt) + criteria
        else:
            compaction += criteria
        answer.append(len(compaction))
    return min(answer)
