import java.util.*;
class Solution {
    public List<Integer> solution(int[] progresses, int[] speeds) {
        Queue<Integer> q = new LinkedList<>();
        List<Integer> ans = new ArrayList<>();
    
        for(int i = 0; i < progresses.length; i++) {
            int days = (100 - progresses[i]) / speeds[i];
            if((100 - progresses[i]) % speeds[i] != 0) {
                days += 1;
            }
            q.add(days);
        }
        
        int n = q.poll();
        int cnt = 1;
        while(!q.isEmpty()) {
            int next = q.poll();
            if(n>= next) {
                cnt+=1;
            } else{
                ans.add(cnt);
                cnt = 1;
                n = next;
            }
        }
        ans.add(cnt);
        // ans.stream().mapToInt(i -> i).toArray();
        return ans;
    }
}