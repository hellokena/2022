def move_hanoi(frm,to,mid,n,answer):
    if n==1: # 다 옮겼다~
        answer.append([frm,to])
        return
    # start에 있던 n을 제외하고 n-1개의 하노이탑을 end로 옮김
    move_hanoi(frm,mid,to,n-1,answer)
    # start번에 있던 n번 하노이탑을 3번으로 옮김
    answer.append([frm,to])
    # mid에 있던 n-1개의 하노이탑을 to로 옮김
    move_hanoi(mid,to,frm,n-1,answer)

def solution(n):
    answer = []
    move_hanoi(1,3,2,n,answer)
    return answer
    
