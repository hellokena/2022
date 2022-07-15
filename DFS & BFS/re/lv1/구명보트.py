def solution(people, limit):
    stack = []
    answer = 0
    people.sort(reverse=True) # 80 70 50 50
    for i in range(len(people)):
        if len(stack) >= 1:
            if stack[-1] + people[i] <= limit:
                stack.pop()
                answer += 1
                continue
        stack.append(people[i])
    if len(stack) != 0: answer += len(stack)
    return answer
