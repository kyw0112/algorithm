from collections import deque
N = int(input())

queue = deque([i for i in range(1, N+1)])
stack = []
for i in range(N-1):
    stack.append(queue.popleft())
    queue.append(queue.popleft())
stack.append(queue.popleft())
print(*stack)