from heapq import heappop, heappush
import sys
heap = []
N = int(sys.stdin.readline().rstrip())

for _ in range(N):

    n =int(sys.stdin.readline().rstrip())

    if n==0:
        if len(heap)==0:
            print(0)
        else:
            print(heappop(heap))

    else:
        heappush(heap, n)