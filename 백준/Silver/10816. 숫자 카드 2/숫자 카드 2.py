# 10815번
import sys
input=sys.stdin.readline


N=int(input())  # 상근이 숫자카드 갯수
A=list(map(int, input().split()))
A1=[0]*10000001
A2=[0]*10000001
# 상근리스트 음수양수 분류
M=int(input()) # 체크 숫자 M 확인
B=list(map(int, input().split()))
for i in A:
    if i >= 0:
        A1[i] += 1
    elif i < 0:
        A2[(-i)] += 1


for j in B:
    if j >= 0:
        print(A1[j], end=' ')

    elif j < 0:
        print(A2[(-j)], end=' ')