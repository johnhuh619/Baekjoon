import java.util.*;
class Solution {
    public int[] solution(int[] prices) {
        int l = prices.length;
        int[] answer = new int[l];
        Stack<Integer> stack = new Stack<>();
        
        for(int i = 0; i< l ; i++){
            while(!stack.isEmpty() && prices[i] < prices[stack.peek()]){
                int idx = stack.pop();
                answer[idx] = i-idx;
            }
            stack.push(i);
        }
        while(!stack.isEmpty()){
            int idx = stack.pop();
            answer[idx] = l-1 - idx;
        }
        return answer;
    }
}