function solution(answers) {
    let n1 = 0;
    let n1_a = 1;
    
    let n2 = 0;
    let n2_a_even = 2;
    let n2_a_odd = 5;
    let n2_a;
    n2_a = n2_a_even;
    
    let n3 = 0;
    let n3_a = 3;
    
    for(let i=0; i < answers.length; i++){
        if(n1_a === answers[i]){
            n1++;
        }
        if(n2_a === answers[i]){
            n2++;
        }
        if(n3_a === answers[i]){
            n3++;
        }

        //1번 수포자 패턴
        if(n1_a === 5){
            n1_a = 1;
        }else{
            n1_a++;          
        }
        
        
        //2번 수포자 패턴
        if(i%2 === 0){
            if(n2_a_odd === 1){
                n2_a_odd = 3;
            }else if(n2_a_odd > 1 && n2_a_odd < 5){
                n2_a_odd++;
            }else{
                n2_a_odd = 1;
            }
            n2_a = n2_a_odd;
        }else{
            n2_a = n2_a_even;            
            
            //3번 수포자 패턴            
            if(n3_a === 3 || n3_a === 5){
                n3_a -= 2;
            }else if(n3_a === 4){
                n3_a++;
            }else{
                n3_a *= 2;
            }            
        }
    }
    let answer = [];
    let answer_arr = [n1, n2, n3];
    let max = Math.max(...answer_arr);
    for(let k = 0; k < answer_arr.length; k++){
        if(answer_arr[k] === max){
            answer.push(k+1);
        }
    }           
    return answer;
}