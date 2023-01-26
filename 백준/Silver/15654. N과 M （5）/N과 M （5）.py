# 15654


from itertools import permutations


N, M=map(int, input().split())
lis=list(map(int, input().split()))


permu_list = list(permutations(lis , M))
permu_list.sort()

for i in range(len(permu_list)):
    for j in range(M):
        print(permu_list[i][j], end=' ')
    print()