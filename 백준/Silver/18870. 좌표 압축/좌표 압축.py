# 18870 좌표압축
import sys



N = int(input())
X = list(map(int, input().split()))
A=X[:]
# 세트로 중복 제거 후 리스트 형변환 -> sort ( 세트는 순서 없기 때문에 중복 제거 하고 소트)
A=set(A)
A=list(A)
A.sort()
B=[ i for i in range(len(A))]
dic=dict(zip(A,B))
for k in range(N):
    print(dic[X[k]], end=' ')
