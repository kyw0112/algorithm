import sys
sys.setrecursionlimit(10**5)
M, N, K = map(int, input().split())

di = [0, 1, 0, -1] # 우하좌상
dj = [1, 0, -1, 0]


area = 0
def dfs(i, j):
    global area
    if li[i][j] == 0:
        if visited[i][j] == False:
            visited[i][j]=True
            area +=1
            for k in range(4):
                if 0 <= i+di[k]<M and 0<= j+dj[k]<N:
                    ni = i + di[k]
                    nj = j + dj[k]

                    dfs(ni, nj)

li = [[0]*(N) for _ in range(M)]
visited = [[False]*(N) for _ in range(M)]
for k in range(K):

    x1, y1, x2, y2 = map(int, input().split())

    for j in range(x1, x2):
        for i in range(y1, y2):

            li[i][j] =1

areali = []
cnt =0
for j in range(0, N):
    for i in range(0, M):
        if visited[i][j] == False and li[i][j] == 0:
            area = 0
            cnt +=1
            dfs(i, j)
            areali.append(area)

areali.sort()
print(cnt)
print(*areali)