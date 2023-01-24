n=1000000
a = [False,False] + [True]*(n-1)
primes=[]

for i in range(2,n+1):
  if a[i]:
    primes.append(i)
    for j in range(2*i, n+1, i):
        a[j] = False

N=int(input())
num=0
for test_case in range(N):

    num=int(input())
    for j in primes:
        if num%j==0:
            print('NO')
            break
        elif j==999983:
            print('YES')
