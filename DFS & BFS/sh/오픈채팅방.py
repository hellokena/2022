def solution(record):
    answer = []
    users = {}
    # 사용자 정보 저장
    for r in record:
        temp = r.split()
        if temp[0] in ['Enter','Change']: users[temp[1]] = temp[2] # 대치 활용
    for r in record:
        temp = r.split()
        if temp[0] == 'Enter': answer.append(users[temp[1]]+"님이 들어왔습니다.")
        elif temp[0] == 'Leave': answer.append(users[temp[1]]+"님이 나갔습니다.")
        # change는 따로 구현 할 필요 없음 -> 사용자 정보 저장에서 활용
    return answer
