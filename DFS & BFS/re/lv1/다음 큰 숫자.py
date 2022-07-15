def solution(n):
    bin_n = bin(n)[2:]
    for i in range(n+1,1000001):
        bin_i = bin(i)[2:]
        if bin_i.count('1') == bin_n.count('1'): 
            return i
