import itertools# N 과 M (1)은 순열 이건 조합

N, M=map(int, input().split())
li=[]
for i in range(1, N+1):
    li.append(i)


new_li=list(itertools.combinations(li, M)) # itertools 이용하여 li리스트에서 M개 순서를 고려하여 뽑는 방법

for j in range(len(new_li)):

    for m in range(M):
        print(new_li[j][m], end=' ')

    print()