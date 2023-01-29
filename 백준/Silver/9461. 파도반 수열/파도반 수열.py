
# 9461 파도반 수열

# P(N) 의 규칙은 P(N) = P( N-5) + P(N-1)

P_li=[0]*102

P_li[1]=1
P_li[2]=1
P_li[3]=1
P_li[4]=2
P_li[5]=2
for j in range(6, 101):
    P_li[j] = P_li[j-5] + P_li[j-1]



T = int(input())

for _ in range(T):
    N = int(input())
    print(P_li[N])
