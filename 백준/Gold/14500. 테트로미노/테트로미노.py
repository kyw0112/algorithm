di = [0, 1, 0, -1] # 우하좌상
dj = [1, 0, -1, 0]
# 바본가? 천잰가? 비지티드 했다가 해제하면 그만이구나 ㅋㅋㅋ 재귀의 아름다움
def dfs(i, j, dsum, cnt):
    global Maxval
                # 방문하지 않았다면... 으로 가면 안되는데 초기화 되어야함
        # 방문처리하고, 거리 4짜리 dfs 반복 돌리기.
    if cnt==4:
        Maxval = max(Maxval, dsum)
        return
    for k in range(4):
        ni = i + di[k]
        nj = j + dj[k]
        if 0 <= ni < N and 0 <= nj < M and not visitied[ni][nj]:
            visitied[ni][nj] = True
            dfs(ni, nj, dsum+arr[ni][nj], cnt+1)
            visitied[ni][nj] = False

def fform(i, j): # 가운데 점을 기준으로 가능한 애들만 전부 다
    global Maxval
    tf = [False]*5
    if 0<=j+1<M:
        tf[1] = True
    if 0<=i+1<N:
        tf[2] = True
    if 0<=j-1<M:
        tf[3] = True
    if 0<=i-1<N:
        tf[4] = True
    if tf[1] and tf[2] and tf[4]:
        Maxval = max(Maxval, arr[i][j]+arr[i+1][j]+arr[i-1][j]+arr[i][j+1])
    if tf[1] and tf[2] and tf[3]:
        Maxval = max(Maxval, arr[i][j] + arr[i + 1][j] + arr[i][j-1] + arr[i][j + 1])
    if tf[2] and tf[3] and tf[4]:
        Maxval = max(Maxval, arr[i][j] + arr[i + 1][j] + arr[i - 1][j] + arr[i][j -1])
    if tf[1] and tf[3] and tf[4]:
        Maxval = max(Maxval, arr[i][j] + arr[i][j-1] + arr[i - 1][j] + arr[i][j + 1])

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

visitied = [[False]*M for _ in range(N)]
Maxval = 0

for i in range(N):
    for j in range(M):
        visitied[i][j] = True
        dfs(i, j, arr[i][j], 1)
        visitied[i][j] = False
        fform(i, j)


print(Maxval)