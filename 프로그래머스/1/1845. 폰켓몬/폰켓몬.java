import java.util.*;

class Solution {
    public int solution(int[] nums) {
        int max = nums.length / 2;
        
        Set<Integer> data = new HashSet<>();
        
        for(int n: nums){
            data.add(n);
        }
        
        int d_size = data.size();
        
        if(d_size > max){
            return max;
        }
        
        return d_size;
    }
}



    