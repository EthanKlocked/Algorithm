def solution(record):
    indata = record
    chk_list = dict()
    
    # rotate backward
    for i in reversed(range(len(indata))): 
        indata[i] = indata[i].split()
        if indata[i][0] != 'Leave': 
            if indata[i][1] not in chk_list: 
                chk_list[indata[i][1]] = indata[i][2] # record the last nickname
            if indata[i][0] == 'Enter': # case Enter
                indata[i][0] = '들어왔습니다.'
            else: # case Change
                del indata[i]
        else: # case Leave
            indata[i][0] = '나갔습니다.'
            
    # rotate forward            
    for i2 in range(len(indata)): 
        indata[i2] = chk_list[indata[i2][1]]+'님이 '+indata[i2][0] 
        
    return indata