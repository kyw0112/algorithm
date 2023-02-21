s = input().split('-') # s 리스트에 담겨용
tmp = sum(map(int, s[0].split('+')))
for i in range(1, len(s)):
    tmp -= sum(map(int,s[i].split('+')))
print(tmp)
