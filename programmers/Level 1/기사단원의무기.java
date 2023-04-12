import java.util.*;

class Solution {
    public int solution(int number, int limit, int power) {
        ArrayList<Integer> list=new ArrayList<>();
        for(int i=1; i<=number; i++){
            int cnt=0;
            for(int j=1; j*j<=i; j++){
                if(j*j == i) cnt++;
                else if(i%j == 0) cnt+=2;
            }         
            list.add(cnt<=limit ? cnt : power);
        }
        return list.stream().mapToInt(Integer::intValue).sum();
    }
}
