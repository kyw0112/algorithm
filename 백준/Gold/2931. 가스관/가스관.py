di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
# n번블럭
block_dic = {
    '.' : 0,
    '|' : 1,
    '-' : 2,
    '+' : 3,
    '1' : 4,
    '2' : 5,
    '3' : 6,
    '4' : 7
}
block_reverse_dic = {

     0 : '.',
     1 : '|',
     2 : '-',
     3 : '+',
     4 : '1',
     5 : '2',
     6 : '3',
     7 : '4'


}




def block_move(i, j, n, moving_vector):
    global tar_i, tar_j
    if n==0:
        tar_i, tar_j = i, j
        return
    if n==1 or n==2 or n==3:
        ni = i + di[moving_vector]
        nj = j + dj[moving_vector]
        block_move(ni, nj, block_dic[arr[ni][nj]], moving_vector)

        # block_move(i+di[moving_vector], j+dj[moving_vector], block_dic[arr[i+di[moving_vector]][j+di[moving_vector]]], moving_vector)

    elif n==4:
        if moving_vector==3: # 무빙벡터 위면
            block_move(i, j+1, block_dic[arr[i][j+1]], 0)
        else:
            block_move(i+1, j, block_dic[arr[i+1][j]], 1)

    elif n==5:
        if moving_vector==1:
            block_move(i, j+1, block_dic[arr[i][j+1]], 0)
        else:
            block_move(i-1, j, block_dic[arr[i-1][j]], 3 )

    elif n==6:
        if moving_vector==0:
            block_move(i-1, j, block_dic[arr[i-1][j]], 3)
        else:
            block_move(i, j-1, block_dic[arr[i][j-1]], 2)

    elif n==7:
        if moving_vector==0:
            block_move(i+1,j,block_dic[arr[i+1][j]], 1)
        else:
            block_move(i, j-1, block_dic[arr[i][j-1]], 2)


R, C = map(int, input().split())

arr = [list(input()) for _ in range(R)]

for i in range(R):
    for j in range(C):
        if arr[i][j]=='M':
            tmp_i, tmp_j = i, j
            break
ganung_li = [

    [],
    [1, 3],
    [0, 2],
    [0, 1, 2, 3],
    [2, 3],
    [1, 2],
    [0, 1],
    [0, 3]

]

name_li =[

    [],
    [1,3],
    [0,2],
    [0,1,2,3],
    [0,1],
    [0,3],
    [2,3],
    [1,2]


]



for k in range(4):
    ni = tmp_i + di[k]
    nj = tmp_j + dj[k]

    if 0<=ni<R and 0<=nj<C:
        if block_dic[arr[ni][nj]]!=0 and (k) in ganung_li[block_dic[arr[ni][nj]]]:
            tmp_k = k
            tmpp_i = ni
            tmpp_j = nj
            break
tar_i, tar_j =0, 0


block_move(ni, nj, block_dic[arr[ni][nj]], k)

k_li = [[2,3,6,7],[1,3,5,6],[2,3,4,5],[1, 3, 4, 7]]
gun_li = []
for k in range(4):
    ni = tar_i + di[k]
    nj = tar_j + dj[k]

    if 0<=ni<R and 0<=nj<C and arr[ni][nj]!='.' and arr[ni][nj]!='M' and arr[ni][nj]!='Z':
        if block_dic[arr[ni][nj]] in k_li[k]:
            gun_li.append(k)

print(tar_i+1, tar_j+1, block_reverse_dic[name_li.index(gun_li)])