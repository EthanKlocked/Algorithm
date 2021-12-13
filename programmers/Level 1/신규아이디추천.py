def solution(new_id):
    # 1단계
    filtered_id = new_id.lower()
    
    # 2단계    
    special_char = '~!@#$%^&*()=+[{]}:?,<>/'
    filtered_id = ''.join(c for c in filtered_id if c not in special_char)
    if len(filtered_id) == 0: 
        return 'aaa'
    
    # 3단계
    filtered_id = list(filtered_id)
    for l in range(len(filtered_id)):        
        if (l == len(filtered_id)-1):
            break
        if(filtered_id[l] == '.' and filtered_id[l+1] == '.'):
            filtered_id[l] = ''
    filtered_id = ''.join(filtered_id)
    
    # 4단계
    if filtered_id[0] == '.':
        if len(filtered_id) == 1:
            return 'aaa'
        filtered_id = filtered_id[1:]    
    if filtered_id[-1] == '.':
        filtered_id = filtered_id[:-1]
        
    # 6단계
    if len(filtered_id) >= 16:
        filtered_id = filtered_id[:15]
        if filtered_id[-1] == '.':
            filtered_id = filtered_id[:14]
            
    #7단계
    if len(filtered_id) == 1:    
        filtered_id = filtered_id + filtered_id[0] + filtered_id[0]
    if len(filtered_id) == 2:    
        filtered_id = filtered_id + filtered_id[1]
        
    return filtered_id