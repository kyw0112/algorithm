person = ['SK', 'CY']
now_person ='SK'
def dol(n,i):

    if n==1 or n==3: # 1이나 3이면 게임 받아온 내가 이겼어
        print(person[i])
        return

    elif n%4==0: # 나눠서 0이면 넘겨준 상대방이 이겼어.
        i = (i+1)%2
        print(person[i])
        return

    if n % 4 == 1: # 1이면 일단 3개빼고 게임 진행시켜
        i = (i+1)%2

        dol(n-3, i)
    elif n%4 ==2: # 나눠서 2면 상대방이 이겼어
        i = (i+1) % 2
        print(person[i])
        return
    elif n%4 == 3: # 3이면 한개빼고 게임 진행시켜
        i = (i + 1) % 2
        dol(n-1, i)


N = int(input())
dol(N, 0)
