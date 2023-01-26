
# 1759 암호만들기
# 최소 한개의 모음과 두개의 자음을 안넣었네
from itertools import combinations
moum=['a','e','i','o','u']
jaum=[chr(j) for j in range(97, 123)] # 아스키코드로 모든 문자 넣은 후 모음 빼자
jaum=list(set(jaum)-set(moum))
jaum.sort()

L, C= map(int, input().split())
li=list(input().split())
li.sort()


com=list(combinations(li, L)) # itertools 컴비네이션으로 뽑은다음 리스트에 넣고 쪼인으로 붙여서 출력
# print(com)

for i in range(len(com)): # 0~ com 길이만큼 체크


    cnt_mo = 0
    cnt_ja = 0
    for z in com[i]:


        if z in moum:
            cnt_mo+=1

        elif z in jaum:
            cnt_ja+=1
        if cnt_ja>1 and cnt_mo>0:
            print(str(''.join(com[i])))
            break