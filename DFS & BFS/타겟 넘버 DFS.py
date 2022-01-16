# dfs
answer = 0
def dfs(num,idx,numbers,target):
    global answer
    if idx == len(numbers)-1:
        if num == target:
            answer += 1
    else:
        dfs(num+numbers[idx+1],idx+1,numbers,target)
        dfs(num-numbers[idx+1],idx+1,numbers,target)
    return answer
            
def solution(numbers, target):
    global answer
    dfs(numbers[0],0,numbers,target) # sum,idx
    dfs(-numbers[0],0,numbers,target)
    print(answer)
    return answer
