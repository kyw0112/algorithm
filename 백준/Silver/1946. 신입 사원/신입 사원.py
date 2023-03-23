import sys
        
T = int(sys.stdin.readline())
for _ in range(T):
    n = int(sys.stdin.readline())
    arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
    arr.sort()

    cnt = 1
    max_num = arr[0][1]
    for i in range(1,n):
        if max_num > arr[i][1]:
            cnt += 1
            max_num = arr[i][1]
            
    print(cnt)