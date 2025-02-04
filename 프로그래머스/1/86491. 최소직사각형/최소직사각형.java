import java.util.*;
class Solution {
    public int solution(int[][] sizes) {
        int longer = 0;
        int shorter = 0;

        for(int[] n: sizes){
            int maxN = Math.max(n[0],n[1]);
            int minN = Math.min(n[0],n[1]);
            longer = Math.max(longer,maxN);
            shorter = Math.max(shorter,minN);
        }
        return longer*shorter;
    }
}