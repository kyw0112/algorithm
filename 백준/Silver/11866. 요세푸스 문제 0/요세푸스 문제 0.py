# 11866 요세푸스 문제0

from collections import deque


N, K = map(int, input().split())

queue = deque(i for i in range(1, N+1))

yose_tmp = 0
yose_li=[]
for _ in range(N):

    for _ in range(K-1):
        tmp=queue[0]
        queue.popleft()
        queue.append(tmp)

    yose_tmp=queue[0]
    yose_li.append(yose_tmp)
    queue.popleft()

print('<',end='')
print(*yose_li, sep=', ', end='')
print('>', end='')
