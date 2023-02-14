dp =[0]+[0 for _ in range(1007)]


dp [1] =1
dp [2] =3

n = int(input())
for i in range(1, 1001):

    dp[i+2] = dp[i+1] + 2*dp[i]


print(dp[n]%10007)