# 2가지 이상 단품메뉴, 2명 이상 손님 주문
from collections import defaultdict,Counter
from itertools import combinations
def solution(orders, course):
    answer = []
    for c in course:
        array = []
        count = defaultdict(int)
        for order in orders:
            order = sorted(order) ##
            # 조합할 땐 sort를 생각해보자
            # 조합을 extend 시키는 것이므로 중복된게 나올 수도 있음 ##
            array += combinations(order,c)
        count = Counter(array)
        #for a in array:
            #count[a] += 1
        #count = dict(sorted(count.items(), key = lambda x:x[1], reverse = True))
        if count:
            if max(count.values()) >= 2:
                for key, value in count.items():
                    if value == max(count.values()):
                        answer.append(''.join(key))
    return sorted(answer)
 
