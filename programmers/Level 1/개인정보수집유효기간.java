import java.util.HashMap;
import java.util.ArrayList;
import java.util.List;
import java.text.SimpleDateFormat;
import java.util.Date;
import java.text.ParseException;

class Solution {
    public List<Integer> solution(String today, String[] terms, String[] privacies) {
        try{
            SimpleDateFormat dateFormat = new SimpleDateFormat("yyyy.MM.dd");
            Date td = dateFormat.parse(today); 
            List<Integer> answer=new ArrayList<>();
            HashMap<String, Integer> ht = new HashMap<>();
            for(String i:terms) ht.put(i.substring(0,1), Integer.parseInt(i.substring(2)));
            int index = 1;
            for(String i:privacies){
                int date = Integer.parseInt(i.substring(8,10));
                int month = Integer.parseInt(i.substring(5,7));
                int year = Integer.parseInt(i.substring(0,4));
                String type = i.substring(11);
                int nextMonth = month + ht.get(type);
                if(nextMonth > 12){
                    year++;
                    nextMonth = nextMonth-12;
                }
                String target = Integer.toString(year)+"."+(nextMonth > 9 ? "" : "0")+Integer.toString(nextMonth)+"."+date;
                Date tg = dateFormat.parse(target);
                if(tg.compareTo(td) <= 0){
                    answer.add(index);
                }
                index++;
            }   
            return answer;     
        }catch(Exception e){
            System.out.println(e.getMessage());
            List<Integer> answer=new ArrayList<>();
            return answer;     
        }
    }
}
