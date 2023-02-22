import sys
from heapq import heappush
from heapq import heappop
arr = []
N = int(sys.stdin.readline().rstrip())
for _ in range(N):
    heappush(arr, int(sys.stdin.readline().rstrip()))
result = 0
for _ in range(N-1):
    a, b = heappop(arr), heappop(arr)
    c = a+b
    result += c
    heappush(arr, c)

print(result)
