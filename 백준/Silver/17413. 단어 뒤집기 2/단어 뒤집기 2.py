# 꺾쇠를 기준으로 꺽쇠 안의 친구들은 큐에 , 나머지는 스택에 넣자
# 근데 어떻게?  넣고 뱉으면서 알아서 하면 그만임 공백이나 '>'가 들어오면
# 걔까지 어펜드 해준다음 전부 다 뱉어서 문자열에 더하면 됨
# 만약 시간초과 난다면 문자열 더하기라서 그런거니까 리스트를 이용해서 하자

from collections import deque
queue = deque()
s = input()
new_s = ''
i=0
stack = []
while i < len(s):
    # print(new_s)
    if s[i] == '<':  # 큐 이용 시작
        while stack:
            new_s += stack.pop()


        while s[i] != '>':
            queue.append(s[i])
            i += 1

        queue.append(s[i])
        i += 1
        while queue:
            new_s += queue.popleft()

    elif s[i] == ' ':

        while stack:
            new_s += stack.pop()
        new_s += ' '
        i += 1

    else:
        stack.append(s[i])
        i += 1
while stack:
    new_s += stack.pop()
print(new_s)