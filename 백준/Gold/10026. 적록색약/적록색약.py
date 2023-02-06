import sys
sys.setrecursionlimit(1000000)
n = int(input())
arr = [list(input()) for _ in range(n)]
visited = [[False]*n for _ in range(n)]

nor_num , R_G_num = 0, 0
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]


def dfs(x, y):

    visited[x][y] = True
    color = arr[x][y]

    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0<= nx < n and 0 <=ny <n :
            if visited[nx][ny]==False:
                if arr[nx][ny] == color:
                    dfs(nx, ny)

for i in range(n):
    for j in range(n):

        if visited[i][j] == False:
            dfs(i, j)
            nor_num +=1

for i in range(n):
    for j in range(n):
        if arr[i][j] == 'R':
            arr[i][j]='G'


visited = [[False] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if visited[i][j] == False:
            dfs(i, j)
            R_G_num +=1


print(nor_num, R_G_num)