from collections import deque

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

def bfs(i, j):
    global chees_chk
    if not visited[i][j] and arr[i][j] == 0:
        visited[i][j]=True
        queue.append((i,j))
        while queue:
            i, j = queue.popleft()

            for k in range(4):
                ni = i + di[k]
                nj = j + dj[k]
                if 0 <= ni < N and 0<=nj<M and not visited[ni][nj] and arr[ni][nj]==0:
                    queue.append((ni, nj))
                    visited[ni][nj] = True
                if 0<=ni<N and 0<=nj<M  and arr[ni][nj] == 1: # 치즈면, 방문배열 그냥 쓰자
                    chees_chk = True # 치즈 찾았다고 체크하고

                    visited[ni][nj] += 1 # 1 더해주고
                    if visited[ni][nj] >= 2:
                        arr[ni][nj] = 0 # 치즈 없애고

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

queue = deque()

cnt = 0
while True:
    visited = [[False] * M for _ in range(N)]
    chees_chk = False
    bfs(0, 0)

    if chees_chk == False:
        break
    cnt += 1


print(cnt)