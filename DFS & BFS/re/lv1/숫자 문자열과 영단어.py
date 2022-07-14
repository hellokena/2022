def solution(s):
    nums = ['zero','one','two','three','four','five','six','seven','eight','nine']
    for num in nums:
        s = s.replace(num,str(nums.index(num)))  
    return int(s)
