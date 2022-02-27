from collections import deque

def solution(n):
    dict = {}
    queue = deque()
    queue.append((1,0)) # 현재 이모티콘수, 클립보드 # queue에 시간 변수를 두는 것이 아니라 dict로 둠
    dict[(1,0)] = 0
    
    while queue:
        e, c= queue.popleft()
        if e == n: # n개 이모티콘 생성
            print(dict[(e,c)])
            break
            
        # 1. 화면에 있는 이모티콘을 모두 복사해서 클립보드에 저장한다
        if (e,e) not in dict.keys():
            dict[(e,e)] = dict[(e,c)] + 1
            queue.append((e,e))
            
        # 2. 클립보드에 있는 모든 이모티콘을 화면에 붙여넣기 한다
        if (e+c,c) not in dict.keys():
            dict[(e+c,c)] = dict[(e,c)] + 1
            queue.append((e+c, c))
            
        # 3. 화면에 있는 이모티콘 중 하나를 삭제한다
        if (e-1,c) not in dict.keys():
            dict[(e-1,c)] = dict[(e,c)] + 1
            queue.append((e-1, c))

n = int(input())
solution(n)
