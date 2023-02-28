memo = {}

def binaryCheck(target):
    if len(target) == 1: return True
    #memo check
    if target in memo: return memo[target]
    #divide
    mid = len(target)//2
    front = target[:mid]
    rear = target[mid+1:]    
    #end check
    if target[mid] == "0" and (front[len(front)//2] == "1" or rear[len(rear)//2] == "1"): return False
    if len(target) == 3: return True
    #return: recursive
    frontChk = binaryCheck(front) 
    rearChk = binaryCheck(rear)
    if not front in memo: memo[front] = frontChk
    if not rear in memo: memo[rear] = rearChk
    return frontChk and rearChk;

def solution(numbers):
    answer = []
    for i in numbers:
        num = bin(i)[2:]
        zeroSupply = ~len(num) & ((1 << len(bin(len(num))[2:])) - 1)
        target = "0"*zeroSupply+num
        answer.append(1 if binaryCheck(target) else 0)   
    return answer
