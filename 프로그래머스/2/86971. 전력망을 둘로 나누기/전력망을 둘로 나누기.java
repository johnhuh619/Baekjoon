import java.util.*;
class Solution {
    static boolean[] visited;
    static int[][] graph;
    
    static int bfs(int n, int c){
        visited = new boolean[n+1];
        int cnt = 1;
        Queue<Integer> q = new LinkedList<>();
        visited[c] = true;
        q.offer(c);
        while(!q.isEmpty()){
            int t = q.poll();
            for(int i=0; i<n+1;i++){
                if(graph[t][i] == 1 && !visited[i]){
                    visited[i] = true;
                    q.offer(i);
                    cnt++;
                }
            }
        }
        return (int)Math.abs(2*cnt - n);
    }
    public int solution(int n, int[][] wires) {
        int ans = (int)1e9;
        graph = new int[n+1][n+1];
        
        for(int[] nums: wires){
            graph[nums[0]][nums[1]] = 1;
            graph[nums[1]][nums[0]] = 1;
        }
        
        for(int[] nums: wires){
            graph[nums[0]][nums[1]] = 0;
            graph[nums[1]][nums[0]] = 0;
            
            ans = Math.min(ans,bfs(n,nums[0]));
            
            graph[nums[0]][nums[1]] = 1;
            graph[nums[1]][nums[0]] = 1;
        }
        
        return ans;
    }
}