import sys

a = sys.stdin.readline().rstrip()
explosion_str = sys.stdin.readline().rstrip()
stack =[]


for i in range(len(a)):

    stack.append(a[i])

    if ''.join(stack[-len(explosion_str):]) ==explosion_str:
        for _ in range(len(explosion_str)):
            stack.pop()
if not stack:
    print('FRULA')
else:
    print(''.join(stack))