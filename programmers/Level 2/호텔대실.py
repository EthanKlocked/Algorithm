def solution(book_time):
    rooms = []
    book_time.sort()
    for i in book_time:
        f = 60*int(i[0][0:2]) + int(i[0][3:5])
        b = 60*int(i[1][0:2]) + int(i[1][3:5])
        if not rooms : rooms.append([(f, b)])
        else :
            for idx, r in enumerate(rooms):
                c = True
                for t in r :
                    if not(t[1] + 10 <= f): 
                        c = False
                        break
                if c : 
                    r.append((f, b))
                    break
                elif idx == len(rooms)-1: 
                    rooms.append([(f, b)])
                    break
    return len(rooms)
