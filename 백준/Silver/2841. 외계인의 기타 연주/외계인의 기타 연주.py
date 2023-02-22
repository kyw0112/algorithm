import sys
stack = [[] for _ in range(7)]


N, P = map(int, sys.stdin.readline().rstrip().split())
finger_cnt = 0
for _ in range(N):
    i, j = map(int, sys.stdin.readline().rstrip().split()) # 음 프랫
    while stack[i] and stack[i][-1]>j:
        stack[i].pop()
        finger_cnt += 1
    if stack[i] and stack[i][-1]==j:
        continue
    stack[i].append(j)
    finger_cnt += 1
print(finger_cnt)