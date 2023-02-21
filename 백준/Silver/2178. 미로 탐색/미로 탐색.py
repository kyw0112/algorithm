# 2차원 구조에서 BFS
from collections import deque
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
def bfs(i, j):

    queue = deque()
    queue.append((i,j))

    while queue:
        i, j = queue.popleft()

        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]

            if ni <0 or ni>=N or nj < 0 or nj>=M: # 행렬 최대 좌표 수정하기
                continue
            if graph[ni][nj] == 1:
                graph[ni][nj] = graph[i][j] + 1
                queue.append((ni, nj))

    return graph[N-1][M-1]


N, M = map(int, input().split())
graph = [list(map(int,input() )) for _ in range(N)]

print(bfs(0,0))