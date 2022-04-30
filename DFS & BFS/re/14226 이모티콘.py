from collections import deque
def solution(s):
    visited = dict()
    queue = deque()
    queue.append((1,0))
    visited[(1,0)] = 0
    while queue:
        emoticon, clipboard = queue.popleft()
        if emoticon == s:
            print(visited[(emoticon,clipboard)])
            return
        if (emoticon, emoticon) not in visited:
            visited[(emoticon,emoticon)] = visited[(emoticon,clipboard)] + 1
            queue.append((emoticon,emoticon))
        if (emoticon+clipboard,clipboard) not in visited:
            visited[(emoticon+clipboard,clipboard)] = visited[(emoticon,clipboard)] + 1
            queue.append((emoticon+clipboard,clipboard))
        if (emoticon-1,clipboard) not in visited:
            visited[(emoticon-1,clipboard)] = visited[(emoticon,clipboard)] + 1
            queue.append((emoticon-1, clipboard))
            
s = int(input())
solution(s)
