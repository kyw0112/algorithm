import sys
input=sys.stdin.readline


N, M = map(int, input().split())
S=[]
gum=[]

for _ in range(N):

    S_str=input()
    S.append(S_str)
cnt=0
for _ in range(M):

    M_str=input()
    if M_str in S:
        cnt+=1


print(cnt)