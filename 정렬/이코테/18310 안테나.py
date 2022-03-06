def solution(n,house):
    house.sort()
    if n%2==0: # 짝수
        print(house[n//2-1]) ## 인덱스로 생각하기!!!!!!!!!
    else: # 홀수
        print(house[n//2])
    ## 애초에 (n-1)//2 하면 더 간단하긴한데!
    # 왜냐면 우리는 인덱스는 0부터 시작인데, 갯수는 1부터 시작이니까... -> 인덱스를 우리 방식대로 변환하자
    # 항상 나누면 앞에께 더 크게 오긴해! -> 작은거 고르랬으니까 이거 사용하는데
    # 짝수개에서 큰걸 선택한다고 하면은 그냥 바로 n//2!

n = int(input())
house = list(map(int, input().split()))
solution(n, house)
