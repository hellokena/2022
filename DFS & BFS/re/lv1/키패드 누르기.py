def solution(numbers, hand):
    keyboard = {'1':(0,0),'2':(0,1),'3':(0,2),
                '4':(1,0),'5':(1,1),'6':(1,2),
                '7':(2,0),'8':(2,1),'9':(2,2),
                '*':(3,0),'0':(3,1),'#':(3,2)}
    answer = ''
    # 현재 손가락 위치
    left_h, left_w = keyboard['*']
    right_h, right_w = keyboard['#']
    for num in numbers:
        num = str(num)
        # 1,4,7의 경우 왼쪽 엄지손가락 사용
        if num in ['1','4','7']: 
            answer += 'L'
            left_h, left_w = keyboard[num]
        # 3,6,9의 경우 오른쪽 엄지손가락 사용
        elif num in ['3','6','9']: 
            answer += 'R'
            right_h, right_w = keyboard[num]
        # 2,5,8,0
        else: 
            now_h, now_w = keyboard[num]
            # 오른손, 왼손 각각 거리 계산
            left_dist = abs(now_h - left_h) + abs(now_w - left_w)
            right_dist = abs(now_h - right_h) + abs(now_w - right_w)     
            if left_dist > right_dist: # 오른손이 더 가까움
                answer += 'R'
                right_h, right_w = keyboard[num]
            elif left_dist < right_dist: # 왼손이 더 가까움
                answer += 'L'
                left_h, left_w = keyboard[num]
            elif left_dist == right_dist:
                if hand == 'right': # 오른손잡이
                    answer += 'R'
                    right_h, right_w = keyboard[num]
                elif hand == 'left': # 왼손잡이
                    answer += 'L'
                    left_h, left_w = keyboard[num]
    return answer
        
