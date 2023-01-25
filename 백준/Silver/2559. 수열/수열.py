
# 2559 수열

N, K= map(int, input().split())

A= list(map(int, input().split()))

S=[sum(A[0:K])] # 초기 항 인덱스 0~ K-1 까지 합
max_sum=S[0] 

for i in range(N-K+1):
    if i<N-K:
        S.append(S[i]+A[i+K]-A[i])
        max_sum=max(max_sum, S[i+1])

print(max_sum)