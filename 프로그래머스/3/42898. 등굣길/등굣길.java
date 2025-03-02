import java.util.*;
class Solution {
    public int solution(int m, int n, int[][] puddles) {
        int mod = 1000000007;
        int answer = 0;
        int [][] dp = new int[n+1][m+1];
        boolean[][] npuddles = new boolean[n+1][m+1];
        for(int[] puddle: puddles){
            npuddles[puddle[1]][puddle[0]] = true;
        }
        dp[1][1] = 1;
        for (int i =0; i<n+1; i++){
            for(int j = 0; j<m+1; j++){
                if(i == 1 && j == 1) continue;
                if(npuddles[i][j]){
                    dp[i][j] = 0;
                } else {
                    int f = (i > 0) ? dp[i-1][j] : 0;
                    int r = (j > 0) ? dp[i][j-1] : 0;
                    dp[i][j] = (f + r) % mod;
                }
            }
        }
        answer = dp[n][m] ;
        return answer;
    }
}