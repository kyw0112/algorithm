# N_Queen problem

def DFS(i):
    global cnt
    if i == N:
        cnt += 1
        return
    for j in range(N):
        if not visited[j]:
            con = False
            for k in range(0, i):
                if plus_daegak[k] == i+j or minus_daegak[k] == j-i:
                    con = True
                    break
            if con:
                continue
            visited[j] = True
            plus_daegak[i] = i+j
            minus_daegak[i] = j-i
            DFS(i+1)
            plus_daegak[i] = 0
            minus_daegak[i] = 0
            visited[j] = False

N = int(input())
visited = [False]*N
plus_daegak = [0]*N
minus_daegak = [0]*N

cnt = 0

DFS(0)

print(cnt)