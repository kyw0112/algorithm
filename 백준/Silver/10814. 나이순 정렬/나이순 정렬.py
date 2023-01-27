#10814 나이순 정렬렬
import sys
input=sys.stdin.readline

N=int(input())
li=[]

for i in range(N):

    li.append(list((input().split())))
    li[i][0] =int(li[i][0])
li.sort(key=lambda x: (x[0]))

for i in range(N):
    print(str(li[i][0]),(li[i][1]))

    