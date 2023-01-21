import sys
input=sys.stdin.readline

T=int(input())

for test_case in range(T):

    s=list((input().split()))

    for i in range(len(s)):

        s[i]=s[i][::-1]

    converge=' '.join(strs for strs in s)
    print(converge)