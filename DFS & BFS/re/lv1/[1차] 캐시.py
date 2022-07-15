def solution(cacheSize, cities):
    # 캐시크기가 0인 경우 다 
    if cacheSize == 0: return len(cities)*5
    answer = 0
    stack = []    
    for city in cities:
        city = city.lower()
        if city in stack: 
            answer += 1 # hit
            stack.remove(city) # stack안에 있는 도시 갱신 위해 지움
        else:  # 현재 캐시에 없는 경우 추가 필요
            if cacheSize == len(stack):
                stack.pop(0) # 처음꺼 캐시 없애기
            answer += 5 # miss
        stack.append(city) # 마지막에 city 추가 - 도시 갱신
    return answer
