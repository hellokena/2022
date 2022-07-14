def solution(board, moves):
    answer = 0
    basket = []
    for move in moves:
        move -= 1 # 인덱스 맞춤
        # 인형을 뽑아 바구니에 넣음
        for i in range(0,len(board[0])):
            if board[i][move] != 0: # 인형이 있을 때까지 
                basket.append(board[i][move])
                board[i][move] = 0 # 뽑았으니까 0 ##
                break
        # 인형이 2개면 pop -> 3개가 쌓일 수가 없음
        # basket [밑....위]
        if len(basket) >= 2:
            if basket[-1] == basket[-2]:
                basket.pop()
                basket.pop()
                answer += 2
    return answer
    
