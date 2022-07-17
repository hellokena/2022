import math
from collections import defaultdict
def solution(fees, records):
    car_time = defaultdict(int)
    cars_info = defaultdict(int)
    for record in records:
        time,car_num,state = record.split()
        if state == 'IN': 
            cars_info[car_num] = 60*int(time[:2]) + int(time[3:])
        elif state == 'OUT':
            # 요금계산
            time = (60*int(time[:2]) + int(time[3:]))-cars_info[car_num]
            car_time[car_num] += time # 누적 요금 따로 저장
            del(cars_info[car_num]) # 출차 완료 차량 삭제
    # 나간 기록이 없는 차들 처리
    for car_num in cars_info:
        time = ((60*23) + 59) - cars_info[car_num]
        car_time[car_num] += time
    for car in car_time:
        if car_time[car] <= fees[0]: # 기본 시간 이하일 경우
            car_time[car] = fees[1] # 기본 요금만 청구
        else: # 기본 시간 이상 주차시
            car_time[car] = fees[1] + math.ceil((car_time[car]-fees[0])/fees[2])*fees[3]
    answer = []
    for i in sorted(car_time.items()): # 딕셔너리 정렬시 dict.items(), key[0], value[1]
        answer.append(i[1])
    return answer
