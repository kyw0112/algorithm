#2309 일곱난쟁이
import sys
input=sys.stdin.readline

height_li=[]


for i in range(9):

    n=int(input())

    height_li.append(n)

for j in range(8):


    for k in range(j+1,9):
        if (sum(height_li)-height_li[j]-height_li[k])==100:
            height_li.remove(height_li[j])
            height_li.remove(height_li[k - 1])  # 하나 리무브 하고나면 인덱스 땡겨지는구나!

            break
    if (len(height_li) == 7):
        break




height_li.sort()

for p in range(len(height_li)):
    print(height_li[p])

