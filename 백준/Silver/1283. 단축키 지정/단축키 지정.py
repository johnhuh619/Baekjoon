def sol():
    n = int(input())
    d = set()
    for _ in range(n):
        l = input()
        words = l.split()
        opt = None

        s = 0
        for w in words:
            idx = l.find(w,s)
            if w[0].lower() not in d:
                d.add(w[0].lower())
                opt = l[:idx] + "[" + l[idx] + "]" + l[idx+1:]
                break
            s = s + len(w)

        if not opt:
            for i, ch in enumerate(l):
                if ch != " " and ch.lower() not in d:
                    d.add(ch.lower())
                    opt = l[:i] + "[" + l[i] + "]" + l[i+1:]
                    break
                    
        if not opt:
            opt = l
        
        print(opt)
  
sol()

      