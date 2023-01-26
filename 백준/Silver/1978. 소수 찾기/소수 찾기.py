# 에라토스테네스 체 구현

chk=[False, False]+[True]*999

prime_li=[]
for i in range(2, 1001):

    if chk[i]:
        prime_li.append(i)
        for j in range(2*i, 1001, i):
            chk[j]=False

N=int(input())
N_li=list(map(int, input().split()))
prime_cnt=0
for j in N_li:
    if chk[j]:
        prime_cnt+=1

print(prime_cnt)
