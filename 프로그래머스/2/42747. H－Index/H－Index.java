import java.util.*;
class Solution {
    public int solution(int[] c) {
        int answer = 0;
        Arrays.sort(c);
        for(int i = 0; i< c.length; i++){
            // 0,1,3,5,6
            int h = c.length - i;
            if(c[i] >= h){
                answer = h;
                break;
            }
        }
        return answer;
    }
}