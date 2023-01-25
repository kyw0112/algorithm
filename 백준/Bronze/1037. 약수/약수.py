import sys
input=sys.stdin.readline

yak_num=int(input())
jin_yak=list(map(int, input().split()))

jin_yak.sort()

print(jin_yak[0]*jin_yak[-1])

