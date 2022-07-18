import copy
def solution(rows, columns, queries):
    answer = []
    # 그래프 생성
    graph = [[0]*columns for _ in range(rows)]
    n = 1
    for i in range(rows):
        for j in range(columns):
            graph[i][j] = n
            n += 1
    
    for h1,w1,h2,w2 in queries:
        h1,w1,h2,w2 = h1-1,w1-1,h2-1,w2-1
        temp = graph[h1][w1]                 
        min_num = temp
    # 방향은 맞게 가되, for문은 거꾸로
    # 왼쪽
        for i in range(h1,h2):          
            graph[i][w1] = graph[i+1][w1]
            min_num = min(min_num, graph[i][w1])
    # 아래쪽
        for i in range(w1,w2):
            graph[h2][i] = graph[h2][i+1]
            min_num = min(min_num, graph[h2][i])
    # 오른쪽
        for i in range(h2,h1,-1):
            graph[i][w2] = graph[i-1][w2]
            min_num = min(min_num,graph[i][w2])
    # 위쪽
        for i in range(w2,w1,-1):
            graph[h1][i] = graph[h1][i-1]
            min_num = min(min_num, graph[h1][i])
            
        graph[h1][w1+1] = temp 
        answer.append(min_num)
    
    return answer
                
    
            
                    
    
    
            
            
    
        
