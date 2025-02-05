import java.util.*;

class Solution {
    static Set<Integer> set;
    static boolean[] visited = new boolean[7];
    
    public static void dfs(String n, String s, int depth){
        if(depth == n.length()) {
            return;
        }
        
        for(int i =0;i <n.length(); i++){
            if(!visited[i]){
                visited[i] = true;
                set.add(Integer.parseInt(s + n.charAt(i)));
                dfs(n, s + n.charAt(i), depth+1);
                visited[i] = false;
            }
        }

    }
    
    public static boolean isPrime(int n){
        if(n < 2){
            return false;
        }
        for(int i = 2; i <= (int)Math.sqrt(n); i++){
            if(n%i==0){
                return false;
            }
        }
        return true;
    }
    
    public int solution(String numbers) {
        int ans = 0;
        set = new HashSet<>();
        dfs(numbers, "", 0);
        
        for(Integer i : set){
            if(isPrime(i)){ 
                ans++;
            }
        }
        return ans;
    }}