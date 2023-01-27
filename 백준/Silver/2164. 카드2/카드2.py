from collections import deque


N = int (input())


queue = deque(i for i in range(1, N+1))

# 1. 제일 왼쪽을 버린다.
# 2. 그다음 제일 왼쪽 카드를 제일 오른쪽으로 옮긴다.
tmp = 0 # 카드 옮기기 위해 저장할 변수

for _ in range(N-1):

    queue.popleft()
    tmp = queue[0]
    queue.append(tmp)
    queue.popleft()

print(queue[0])