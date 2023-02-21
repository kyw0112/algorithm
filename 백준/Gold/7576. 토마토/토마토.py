from collections import deque
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

M, N = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
queue = deque()
for i in range(N):
    for j in range(M):
        if graph[i][j]==1:
            queue.append((i,j))
max = 1
while queue:
    i, j = queue.popleft()

    for k in range(4):
        ni = i + di[k]
        nj = j + dj[k]

        if ni <0 or ni>=N or nj < 0 or nj>=M: # 행렬 최대 좌표 수정하기
            continue
        if graph[ni][nj] == 0:
            graph[ni][nj] = graph[i][j] + 1
            queue.append((ni, nj))
            if graph[ni][nj]>max:
                max = graph[ni][nj]


for i in range(N):
    for j in range(M):
        if graph[i][j] == 0:
            print(-1)
            break
    if graph[i][j] == 0:
        break
else:
    if max==1:
        print(0)
    else:
        print(max-1)
