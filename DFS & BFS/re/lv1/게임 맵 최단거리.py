from collections import deque
def solution(maps):
    h,w = len(maps), len(maps[0])
    #visited = [[0]*w for _ in range(h)]
    queue = deque()
    queue.append((0,0))
    #visited[0][0] = 1
    while queue:
        nowh, noww = queue.popleft()
        if nowh == h-1 and noww == w-1: return maps[-1][-1]
        dh = [-1, 1, 0, 0]
        dw = [0, 0, -1, 1]
        for d in range(4):
            nexth = nowh + dh[d]
            nextw = noww + dw[d]
            if 0<=nexth<h and 0<=nextw<w and maps[nexth][nextw] == 1:
                maps[nexth][nextw] = maps[nowh][noww] + 1
                queue.append((nexth,nextw))
    return -1
