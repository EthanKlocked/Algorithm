def solution(numbers):
    answer = []
    numbers.reverse()
    for i in range(len(numbers)):
        if i == 0 : addNum = (-1, 0)
        elif numbers[i] < numbers[i-1] : addNum = (numbers[i-1], i-1)
        elif numbers[i] > numbers[i-1] : 
            chkIndex = i-1
            while True:
                chkValue = answer[chkIndex][0]
                if chkValue == -1:
                    addNum = (-1, 0)
                    break
                elif numbers[i] < chkValue :
                    addNum = (chkValue, answer[chkIndex][1])
                    break
                else: chkIndex = answer[chkIndex][1]
        answer.append(addNum)
    answer.reverse()
    return [x[0] for x in answer]
