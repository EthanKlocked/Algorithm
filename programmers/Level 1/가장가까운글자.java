import java.util.*;

class Solution {
    public ArrayList<Integer> solution(String s) {
        ArrayList<Integer> answer = new ArrayList<>();
        HashMap<Character,Integer> ht = new HashMap<>();
        for(int i=0; i<s.length(); i++){
            char target = s.charAt(i);
            if(!ht.containsKey(target)) answer.add(-1);
            else answer.add(i-ht.get(target));
            ht.put(target, i);
        }
        return answer;
    }
}
