def gcd(x,y):
    while(y):
        x,y=y,x%y
    return x
    
def blank(w,h):
    big, small = max(w,h),min(w,h)
    return min(w,h)*(big//small+1)+(big%small-1)

def solution(w,h):
    cf = gcd(w,h)
    if(cf != 1):
        return w*h-cf*blank(w/cf,h/cf)
    return w*h-blank(w,h)
