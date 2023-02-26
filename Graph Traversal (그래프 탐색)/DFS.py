graph=[[] for _ in range(5)]
visited=[False]*5

#DFS는 스택을 이용한다
def dfs(graph,visited,v):
    visited[v]=True
    print(v,end=" ")

    #현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph,visited,i)