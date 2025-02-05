class Solution {
    static boolean[] visited;
    static int count = 0;   
    static void dfs(int hp, int[][] dungeons, int depth){        
        for(int i =0; i<dungeons.length;i++){
            if(visited[i] || dungeons[i][0] > hp){
                continue;
            }
            visited[i] = true;
            dfs(hp - dungeons[i][1], dungeons, depth+1);
            visited[i] = false;
        }
        count = Math.max(count,depth);
    }
    public int solution(int k, int[][] dungeons) {
        visited = new boolean[dungeons.length];
        dfs(k,dungeons,0);
        return count;
    }
}

// 피로도 => 
// 최소 피로도 / 소모 피로도
// 조건 b 가 a 에 영향을 미친다.
