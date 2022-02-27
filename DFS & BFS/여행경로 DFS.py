def solution(tickets):
    answer = []
    
    tickets.sort(key=lambda x:(x[1]), reverse = True)
    graph = {}
   
    for t1, t2 in tickets:
        if t1 in graph.keys():
            graph[t1].append(t2)
        else:
            graph[t1] = [t2]
    
    stack = ['ICN']
    
    while stack:
        top = stack[-1]
        if top not in graph.keys() or len(graph[top]) == 0: # 해당 출발지에서 시작하는 티켓이 없거나, 아예 해당 출발지에서 시작하는 경우 자체가 없는 경우
            answer.append(stack.pop())
        else: stack.append(graph[top].pop())
    answer.reverse()
    return answer
