def solution(n, arr1, arr2):
    # 그래프 생성
    arr1_graph, arr2_graph = [], []
    for a1,a2 in zip(arr1,arr2):
        binary_a1 = bin(a1)[2:]
        binary_a2 = bin(a2)[2:]
        if len(binary_a1)<n: binary_a1 = '0'*(n-len(binary_a1)) + binary_a1
        if len(binary_a2)<n: binary_a2 = '0'*(n-len(binary_a2)) + binary_a2
        arr1_graph.append(list(map(int,binary_a1)))
        arr2_graph.append(list(map(int,binary_a2)))
    for i in range(n):
        for j in range(n):
            if arr2_graph[i][j] == 1: arr1_graph[i][j] = 1
    answer = []
    for i in range(n):
        temp = ''
        for j in range(n):
            if arr1_graph[i][j] == 0: temp += ' '
            elif arr1_graph[i][j] == 1: temp += '#'
        answer.append(temp)
    return answer
  
  # 사람들 재능 미쳤다... 비트 연산 zfill 함수도 알아감 # 속도도 효율적...
  def solution(n, arr1, arr2):
    # 그래프 생성
    answer = []
    for a1,a2 in zip(arr1,arr2):
        now_row = bin(a1|a2)[2:]
        now_row = now_row.zfill(n)
        now_row = now_row.replace('0',' ')
        now_row = now_row.replace('1','#')
        answer.append(now_row)
    return answer
   
        
