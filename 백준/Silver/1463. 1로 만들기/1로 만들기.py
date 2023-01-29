# 1463 1 DP 공부

N = int(input())



DP = [0] *1000002

if N==1:
    print(DP[1])


else:
    for i in range(2, N+1):

        DP[i] = DP [i-1] +1


        if i%2==0:
            DP[i] = min( DP[i], DP[i//2]+1 )
        if i%3==0:
            DP[i] = min( DP[i], DP[i//3]+1)


    print(DP[i])