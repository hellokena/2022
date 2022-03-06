def solution(n):
    cnt = 0 # 갈 수 있는 경우의 수
    x = int(n[1])
    y = ord(n[0])-96
    
    # 방향벡터
    dx = [-2, -1, 1, 2, 2, 1, -1, -2]
    dy = [1, 2, 2, 1, -1, -2, -2, -1]
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
        if 1<=nx<=8 and 1<=ny<=8: cnt += 1
    print(cnt)

n = input()
solution(n)
