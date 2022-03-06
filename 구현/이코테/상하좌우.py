def solution(n, direction):
    x,y = 1,1
    # 방향벡터
    temp = ['L','R','U','D']
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    for d in direction:
        for i in range(4):
            if d==temp[i]:
                nx = x + dx[i]
                ny = y + dy[i]
                if 1<=nx<=n and 1<=ny<=n:
                    x,y = nx,ny
                    break
    print(x,y)

n = int(input())
direction = input().split()
solution(n, direction)
