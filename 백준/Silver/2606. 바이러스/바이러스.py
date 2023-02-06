cnt =0
def dfs(graph, v, visited):
    global cnt
    visited[v] = True
    cnt += 1
    # print(v, end=' ')

    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)
    return cnt

N = int(input())
M = int(input())
graph=[[] for i in range(N+1)]
visited=[False]*(N+1)


for _ in range(M):

    a_i, b_i = map(int, input().split())
    graph[a_i] += [b_i]
    graph[b_i] += [a_i]

print(dfs(graph, 1, visited)-1)