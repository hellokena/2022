def solution(nums):
    poketmon_types = set(nums) # 중복제거
    if len(nums)//2 >= len(poketmon_types):
        return len(poketmon_types)
    else: return len(nums)//2
    # 포켓몬의 최대 종류를 가져가려면 최대한 다 다른 종류로!
    # 만약 포켓몬 종류가 가져가려는 포켓몬 갯수보다 적거나 같으면 어쨋든 포켓몬 종류가 겹칠 수 밖에 없으므로 포켓몬의 모든 종류를 다 가져가는 것이 유리
    # 만약 포켓몬 종류가 가져가려는 포켓몬 수보다 크면 최대한 다 다른 종류를 가져가도록 하는게 유리하므로 포켓몬을 가져가는 갯수인 n//2개의 포켓몬 종류를 가져가는것
