from heapq import heappop, heappush
import sys
maxheap = [] # 왼쪽 힙
minheap = [] # 오른쪽 힙

N = int(sys.stdin.readline().rstrip())

# 왼 오 왼 오 넣을건데, while문 돌면서 왼쪽 맥스가 더 크면 계속 교환 만들어주자

for i in range(N):
    n = int(sys.stdin.readline().rstrip())
    if i%2:
        heappush(maxheap, -n)
    else:
        heappush(minheap, n)

    while maxheap and minheap and -maxheap[0] > minheap[0]:
        tmp1 = heappop(maxheap)
        tmp2 = heappop(minheap)
        heappush(minheap, -tmp1)
        heappush(maxheap, -tmp2)

    if i%2:
        print(-maxheap[0])
    else:
        print(minheap[0])
