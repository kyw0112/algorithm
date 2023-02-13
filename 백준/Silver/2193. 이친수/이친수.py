# 일단 메모이제이션

chin = [[0,0] for _ in range(92)]
chin[1] = [0, 1] # 0끝 개수 1끝 개수
N= int(input())

for i in range(1, N):

    chin[i+1][0], chin[i+1][1] = chin[i][0]+chin[i][1], chin[i][0]

print(sum(chin[N]))