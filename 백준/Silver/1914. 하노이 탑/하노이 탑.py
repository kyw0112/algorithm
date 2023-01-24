
def hanoi(n, from_num, to_num, ass_num):


    if n==1:
        print(from_num, to_num)
        return

    hanoi(n-1, from_num, ass_num, to_num)

    print(from_num, to_num)

    hanoi(n-1, ass_num, to_num, from_num)


n=int(input())
print(2**n-1)
if n<21:
    hanoi(n,1,3,2)
