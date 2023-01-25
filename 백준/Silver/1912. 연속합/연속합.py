n=int(input())

A=list(map(int, input().split()))

S=[A[0]]

for i in range(len(A)-1 ):

    S.append(max(S[i]+A[i+1], A[i+1] ))

print(max(S))