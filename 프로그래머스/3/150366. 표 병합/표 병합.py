def solution(commands):
    answer = []
    parent = [[(r,c) for c in range(51)] for r in range(51)]
    value = [["" for _ in range(51)] for _ in range(51)]
    
    def find(r, c):
        pr, pc = parent[r][c]
        if (pr, pc) == (r, c):
            return (r, c)
        parent[r][c] = find(pr, pc)
        return parent[r][c]
    
    def union(r1, c1, r2, c2):
        r1, c1 = find(r1, c1)
        r2, c2 = find(r2, c2)
        
        if (r1, c1) == (r2, c2):
            return 
        
        if value[r1][c1] == "" and value[r2][c2] != "":
            value[r1][c1] = value[r2][c2]
        value[r2][c2] = value[r1][c1]
        
        parent[r2][c2] = (r1, c1)
    
    def update_v(r, c, v):
        r, c = find(r, c)
        value[r][c] = v
    
    def update_all(v1, v2):
        for i in range(1,51):
            for j in range(1,51):
                r, c = find(i,j)
                if value[r][c] == v1:
                    value[r][c] = v2
    
    
    def unmerge(r, c):
        r_root, c_root = find(r,c)
        saved_value = value[r_root][c_root]
        merged = []
        for i in range(1, 51):
            for j in range(1, 51):
                if find(i, j) == (r_root, c_root):
                    merged.append((i, j))
        
        for i, j in merged:
            parent[i][j] = (i, j)
            value[i][j] =""
        
        value[r][c] = saved_value
           
    
    for cmds in commands:
        parts = cmds.split()

        # "UPDATE r c value"
        # "UPDATE value1 value2"
        if parts[0] == "UPDATE":
            if len(parts) > 3:
                r, c, v = int(parts[1]), int(parts[2]), parts[3]
                update_v(r,c,v)
            else:
                v1, v2 = parts[1], parts[2]
                update_all(v1, v2)

        # "MERGE r1 c1 r2 c2"
        elif parts[0] == "MERGE":
            r1, c1, r2, c2 = map(int, parts[1:])
            union(r1, c1, r2, c2)

        # "UNMERGE r c"
        elif parts[0] == "UNMERGE":
            r, c = int(parts[1]), int(parts[2]),
            unmerge(r, c)
        # "PRINT r c"
        elif parts[0] == "PRINT":
            r, c = int(parts[1]), int(parts[2]),
            r, c = find(r, c)
            ans = value[r][c] if value[r][c] != "" else "EMPTY"
            answer.append(ans)
    return answer