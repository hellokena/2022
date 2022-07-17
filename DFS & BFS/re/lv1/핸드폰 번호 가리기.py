def solution(phone_number):
    idx = len(phone_number)-4
    phone_number = phone_number.replace(phone_number[:idx],'*'*idx)
    return phone_number
    
def solution(phone_number):
    return '*'*(len(phone_number)-4)+phone_number[-4:]
