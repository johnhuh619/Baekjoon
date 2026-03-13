def sol():
    while True:
        n, m = map(int, input().split())
        if n+m == 0:
            break
        graph = []
        all = 0
        for _ in range(m):
            u, v, w = map(int, input().split())
            graph.append((w,u,v))
            all += w 

        graph.sort()

        parent = list(range(n+1))

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(a,b):
            ra = find(a)
            rb = find(b)
            
            if ra == rb:
                return False
            parent[ra] = rb
            return True

        tot = 0
        for w, u, v in graph:
            if union(u,v):
                tot += w
        print(all - tot)
        
sol()