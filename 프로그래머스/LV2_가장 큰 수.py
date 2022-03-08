def solution(numbers):
    temp = list(map(str, numbers))
    temp.sort(reverse=True, key=lambda x:x*3 )
    return str(int(''.join(temp))) # 왜 int후 str? -> 모든값이 0일때는 0으로 하려고
