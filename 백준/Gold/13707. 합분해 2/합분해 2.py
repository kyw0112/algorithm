from math import factorial
import sys
input=sys.stdin.readline

def nCr(n, r):
    if r > n:
        return 0
    else:
        return factorial(n)//factorial(r)//factorial(n-r)  # nCr


N, K=map(int, input().split())

print(nCr(K+N-1,N)%1000000000)