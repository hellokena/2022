def solution(n,house):
    house.sort()
    if n%2==0: # 짝수
        print(house[n//2-1]) ## 인덱스로 생각하기!!!!!!!!!
    else: # 홀수
        print(house[n//2])
    ## 애초에 (n-1)//2 하면 더 간단하긴한데!
    # 왜냐면 우리는 인덱스는 0부터 시작인데, 갯수는 1부터 시작이니까...
    # 항상 나누면 앞에께 더 크게 오긴해!

n = int(input())
house = list(map(int, input().split()))
solution(n, house)
