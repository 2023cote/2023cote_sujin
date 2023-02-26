graph=[[] for _ in range(5)]
visited=[False]*5

#BFS는 큐를 이용한다
from collections import deque
def bfs(graph,visited,v):
    queue=deque([v])
    visited[v]=True
    
    #큐가 빌때까지 반복
    while queue:
        now=queue.popleft()
        print(now,end=" ")

        for i in graph[now]:
            if not visited[i]:
                queue.append(i)
                visited[i]=True