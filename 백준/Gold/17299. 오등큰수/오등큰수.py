n = int(input())
numbers = list(map(int,input().split()))

# 1 1 2 3 4 2 1
# 1-3, 2-2, 3-1, 4-1

n_docs = {}
for num in numbers:
    n_docs[num] = n_docs.get(num, 0) + 1

stack = []
ans = [-1]*n

for i in range(n):
    while stack and n_docs[numbers[stack[-1]]] < n_docs[numbers[i]]:
        idx = stack.pop()
        ans[idx] = numbers[i]
    stack.append(i)

print(*ans)