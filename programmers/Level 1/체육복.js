function solution(n, lost, reserve) {
    let re_lost = lost.filter(x => !reserve.includes(x)).sort();
    let re_reserve = reserve.filter(x => !lost.includes(x)).sort();
    let normal = n - re_lost.length;
    re_lost.forEach((n, i) =>{
        let chk = 0;                    
        re_reserve.forEach((n2,i2) => {
            if(chk == 0){
                let chk_num = Math.floor((n+n2)/2);
                if(chk_num === n || chk_num === n2){
                    chk = 1;                                    
                    normal += 1;
                    re_reserve.splice(i2,1);
                }            
            }
        });
    });
    return normal;
}