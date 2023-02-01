N = int(input())
A_li = list(map(int, input().split()))

NGE_li = [0] *N
stack = []
stack.append(N-1)
for i in range(N-2, -1, -1):

    while stack and A_li[stack[-1]] < A_li[i]:
        NGE_li[stack.pop()] = i+1

    stack.append(i)

print(*NGE_li)