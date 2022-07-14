from collections import defaultdict
def solution(record):
    people = defaultdict(str)
    for rec in record:
        now_rec = rec.split()
        if now_rec[0] == 'Enter':
            people[now_rec[1]] = now_rec[2]
        #elif now_rec[0] == 'Leave':
            #del(people[now_rec[1]])
        elif now_rec[0] == 'Change':
            people[now_rec[1]] = now_rec[2] # 치환 
    answer = []
    for rec in record:
        now_rec = rec.split()
        if now_rec[0] == 'Enter':
            answer.append(people[now_rec[1]] + '님이 들어왔습니다.')
        elif now_rec[0] == 'Leave':
            answer.append(people[now_rec[1]] + '님이 나갔습니다.')
    return answer
        
    
