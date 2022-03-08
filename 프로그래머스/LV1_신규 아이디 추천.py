def solution(new_id):
    new_id = new_id.lower() # 1단계
    remove = ['-','_','.']
    for i in new_id: # 2단계
        if not i.islower() and not i.isdigit() and i not in remove:
            new_id = new_id.replace(i,'')
    while '..' in new_id:
        new_id = new_id.replace('..','.')  # 3단계
    new_id = new_id.strip('.') # 4단계
    if len(new_id) == 0: new_id = 'a' # 5단계
    if len(new_id) >= 16: # 6단계
        new_id = new_id[0:15] 
        new_id = new_id.rstrip('.')
    if len(new_id)<=2: 
        while len(new_id) <= 2:
            new_id += new_id[-1]
    return new_id
