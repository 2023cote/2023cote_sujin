from collections import deque

n=int(input())
visited=[0]*(n+1)
graph=[]

def bfs(v):
    queue=deque([v])
    visited[v]=1

    while queue:
        now=queue.popleft()
        for i in graph[now]:
            if not visited[i]:
                queue.append(i)
                visited[i]=1

def dfs(v):
    visited[v]=1

    for i in graph[v]:
            dfs(i)