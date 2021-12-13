function solution(nums) {
    let val1, val2, val3, last_val, chk;
    let cnt = 0;
    let arr = nums.slice();
    for(let i=0; i < arr.length; i++){
      val1 = arr[i];
      for(let i2=i+1; i2 < arr.length; i2++){
        val2 = arr[i2];  
        for(let i3 = i2+1; i3 < arr.length; i3++){
          val3 = arr[i3];
          last_val = val1 + val2 + val3;
          chk = 0;
          for(let i4 = 2; i4 <= Math.sqrt(last_val); i4++){
            if(last_val%i4 === 0){
              chk = 1;
            }
          }
          if(chk === 0){
            cnt++;
          }
        }          
      }
    }
    return cnt;
  }