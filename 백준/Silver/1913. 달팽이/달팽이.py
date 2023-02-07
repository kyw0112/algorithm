
# 달팽이 정렬


di = [1, 0, -1, 0] # 상우하좌 # 하우상좌
dj = [0,1, 0, -1]

N = int(input())
K = int(input())
i, j = 0, 0
k = 0
em_li = [[0]*N for _ in range(N)]
for n in range((N**2), 0, -1):
    em_li[i][j] = n
    if n==K:
        r_i, r_j = i , j
    if 0<= i + di[k]<N and 0<= j+dj[k]<N and em_li[i + di[k]][j+dj[k]]==0:
        i = i+ di[k]
        j = j+ dj[k]

    else:
        k+=1
        k%=4
        i = i + di[k]
        j = j + dj[k]

for i in range(N):
    print(*em_li[i])
print(r_i+1, r_j+1)