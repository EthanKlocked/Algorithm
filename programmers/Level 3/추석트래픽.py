def solution(lines):
    # 1. Only one data
    if len(lines) == 1:
        return 1
    
    # 2. more than one
    ## (1) raw data -> milli data
    milli_box = []
    for i in lines:
        hours = int(i[11:13])
        mins = int(i[14:16])
        secs = int(i[17:19])
        millisecs = int(i[20:23])
        
        end_point = ((hours*60*60) + (mins*60) + (secs)) * 1000 + millisecs
        
        delay = int(i[24:25])*1000
        if i[25:26] != 's':
            delay += int(i[26:27])*100
            if i[27:28] != 's':
                delay += int(i[27:28])*10
                if i[28:29] != 's':
                    delay += int(i[28:29])
        
        start_point = end_point - delay + 1
        
        milli_box.append((start_point, end_point))
        
    ## (2) SEARCH & CNT : ONLY (start_point[SEARCH]) is equal to end_point of the data
    total_cnt = 1
    
    for k in range(len(milli_box)-1):
        front_sec = milli_box[k][1] #start point [SEARCH]
        end_sec = front_sec+999 #end point [SEARCH]
        now_cnt = 1
        for k2 in range(k+1, len(milli_box)):
            now_front = milli_box[k2][0] #start point [data] 
            if (now_front <= end_sec):
                now_cnt += 1
        if now_cnt > total_cnt:
            total_cnt = now_cnt
    
    return total_cnt