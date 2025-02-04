import java.util.*;
class Solution {
    public int solution(int[] priorities, int loc) {
        List<Integer> list = new ArrayList<>();
        for(int p: priorities){
            list.add(p);
        }
        // LOC을 계속 바꿔야 할듯
        int answer = 0;
        
        while(loc >= 0){
            int max = Collections.max(list);
            if(list.get(0) >= max){
                list.remove(0);
                answer += 1;
                loc -=1;
                if(loc < 0){
                    break;
                }
            } else{ 
                int tmp = list.get(0);
                list.remove(0);
                list.add(tmp);    
                loc-=1;
                if(loc<0){
                    loc = list.size() - 1;
                }
            }
        }
        return answer;
    }
}