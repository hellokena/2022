# my
def solution(lottos, win_nums):
    match = 0 
    for i in lottos:
        if i in win_nums:
            match += 1
    best = min(6, 7 - (match + lottos.count(0)))
    worst = min(6, (7- match))
    return [best,worst]
  
  #ans
  def solution(lottos, win_nums):

    rank=[6,6,5,4,3,2,1]

    cnt_0 = lottos.count(0)
    ans = 0
    for x in win_nums:
        if x in lottos:
            ans += 1
    return rank[cnt_0 + ans],rank[ans]
