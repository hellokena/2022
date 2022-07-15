def solution(n, words):
    answer = []
    end = words[0][-1]
    for i in range(1,len(words)):
        if len(words[i]) > 1 and words[i][0] == end and words[i] not in words[:i]: 
            end = words[i][-1]
        else: # 틀린 경우
            answer.append((i%n)+1)
            answer.append((i//n)+1)
            break
    if len(answer) == 0: return [0,0]
    else: return answer
            
        
