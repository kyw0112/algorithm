N = int(input())
A_li = list(map(int, input().split()))

NGE_li = [-1] *N
stack = []
stack.append(0)
for i in range(1, N):

    while stack and A_li[stack[-1]] < A_li[i]:
        NGE_li[stack.pop()] = A_li[i]

    stack.append(i)

print(*NGE_li)