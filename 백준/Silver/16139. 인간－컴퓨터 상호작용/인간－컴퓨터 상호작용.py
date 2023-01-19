import sys
input=sys.stdin.readline


S=input() # 문자열 S 입력

q=int(input())



for test_case in range(q):

    alpha, l, r =input().split()

    print(S[int(l):int(r)+1].count(alpha))