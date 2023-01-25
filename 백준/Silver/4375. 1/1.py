# 4375 1
# 어이없게 맞춰버림 ㅋㅋㅋㅋ

import sys

for n in sys.stdin: # 테케 무한히 많이 받는 방법

    n= int(n)

    for i in range(1,1000000): # 1의 갯수를 늘려가며 n으로 나눠 떨어지는 순간이 발견되면 1의 개수 i 찍고 break
        s='1'*i
        s=int(s)

        if s%n==0:
            print(i)
            break