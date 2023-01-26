# 에라토스테네스 체 구현

chk=[False, False]+[True]*1000000

prime_li=[]
for i in range(2, 1000001):

    if chk[i]:
        prime_li.append(i)
        for j in range(2*i, 1000001, i):
            chk[j]=False

M, N= map(int, input().split())


for j in range(M, N+1):
    if chk[j]:
        print(j)