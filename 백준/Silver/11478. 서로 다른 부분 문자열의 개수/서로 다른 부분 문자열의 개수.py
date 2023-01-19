
S=input()
sett=set()
tmp=''
for i in range(len(S)):

    for j in range(i,len(S)+1):
        tmp=S[i:j+1]
        sett.add(tmp)


print(len(sett))