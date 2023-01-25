K=int(input())

def hanoi(N,from_pos, to_pos, ass_pos):

    if N==1:
        print(from_pos, to_pos)
        return


    hanoi(N-1, from_pos, ass_pos, to_pos)
    print(from_pos, to_pos)
    hanoi(N-1, ass_pos, to_pos, from_pos)

print(2**K-1)
hanoi(K, 1, 3, 2)