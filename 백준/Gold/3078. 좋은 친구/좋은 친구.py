import sys
from collections import deque
N , K =map(int, sys.stdin.readline().rstrip().split())
arr = [0]*21
queue = deque()
cnt = 0

for i in range(K+1):
    s = sys.stdin.readline().rstrip()
    length =len(s)
    queue.append(length)
    arr[length] +=1
    cnt += arr[length]-1
for i in range(K+1, N):
    s = sys.stdin.readline().rstrip()
    length = len(s)
    arr[queue.popleft()] -=1
    queue.append(length)
    arr[length] += 1
    cnt += arr[length]-1
print(cnt)