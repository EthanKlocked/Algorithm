function solution(price, money, count) {
    var answer = (price + price*count)*count/2-money; // 가우스의 정리
    if(answer < 0){ // 0 예외 처리
        answer = 0;
    }
    return answer;
} 