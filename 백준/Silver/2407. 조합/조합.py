def fc(N):
    global fac
    if N<2: return 1

    fac=1
    for i in range(1, N + 1):
        fac *= i
    return fac

def com(n, r):
    return fc(n)//fc(r)//fc(n-r)



n, r=map(int, input().split())
d=com(n,r)
#nCr=len(list(itertools.combinations(range(b), a)))
print(d)