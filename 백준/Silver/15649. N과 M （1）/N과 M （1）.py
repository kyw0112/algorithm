# 15649 백트래킹 스타트? itertools로 풀면 안되는건가

import itertools

N, M=map(int, input().split())
li=[]
for i in range(1, N+1):
    li.append(i)


new_li=list(itertools.permutations(li, M)) # itertools 이용하여 li리스트에서 M개 순서를 고려하여 뽑는 방법

for j in range(len(new_li)):

    for m in range(M):
        print(new_li[j][m], end=' ')

    print()
