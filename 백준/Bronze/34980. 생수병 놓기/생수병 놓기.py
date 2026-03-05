n = int(input())
before = input()
after = input()

cnt = 0
for ch in before:
    if ch == "w":
        cnt += 1
        
for ch in after:
    if ch == "w":
        cnt -= 1

if cnt == 0:
    if before == after:
            print("Good")
    else:
        print("Its fine")
elif cnt < 0:
    print("Manners maketh man")
else:
    print("Oryang")
