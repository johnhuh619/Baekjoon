import sys
sys.setrecursionlimit(3000)

def solution(n, m, x, y, r, c, k):
    answer = ''
    
    dir = [(1, 0, 'd'), (0, -1, 'l'), (0, 1, 'r'), (-1, 0, 'u')]
    
    def dist(a,b,c,d):
        return abs(a-c) + abs(b-d)
    
    def dfs(cx, cy, steps, path):
        left = k - steps
        
        # E => (r,c)
        d = dist(cx, cy, r, c)
        
        # 종료 조건
        if d > left:
            return None
        
        if (left - d) % 2 != 0:
            return None
        
        if steps == k:
            if cx == r and cy == c:
                return path
            return None
        
        for dx, dy, np in dir:
            nx, ny = cx + dx, cy + dy
            if 1 <= nx <= n and 1 <= ny <= m:
                res = dfs(nx, ny, steps + 1, path + np)
                if res:
                    return res
        return None
    
    ans = dfs(x,y,0,"")
    
    return ans if ans else "impossible"

