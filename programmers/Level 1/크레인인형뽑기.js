function solution(board, moves) {
    // 빈 박스만들기
    let box = [];
    for(let j = 0; j < board.length; j++){
        let semi_box = [];
        box.push(semi_box);
    }    
    // 인형 재배치 박스
    for(let k = 0; k < board.length; k++){
        for(let k2 = 0; k2 < board[k].length; k2++){
            let src = board[k][k2];
            if(src !== 0){
                box[k2].push(src);
            }
        }
    }
    
    // 인형뽑기 시뮬레이션
    let cnt = 0;
    let now_val, next_val;
    let chk_box = [];
    for(let i = 0; i < moves.length; i++){
        let first = box[moves[i]-1];
        if(first.length > 0){
            chk_box.push(first[0]);
            first.shift();
        }
    }
    
    // 결과 필터링
    for(let i2 = 0; i2 < chk_box.length; i2++){
        if(chk_box.length > 1){
            if(chk_box[i2] === chk_box[i2+1]){
                cnt += 2;
                chk_box.splice(i2,2); 
                i2 -= 2;
            }            
        }
    }
    return cnt;
}