"""
문제
그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오. 단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고, 더 이상 방문할 수 있는 점이 없는 경우 종료한다. 정점 번호는 1번부터 N번까지이다.

입력
첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000), 탐색을 시작할 정점의 번호 V가 주어진다. 다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다. 어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다. 입력으로 주어지는 간선은 양방향이다.

출력
첫째 줄에 DFS를 수행한 결과를, 그 다음 줄에는 BFS를 수행한 결과를 출력한다. V부터 방문된 점을 순서대로 출력하면 된다.
"""
"""
배열 선언할 때 * 연산자 쓰는거 지양해야 함
"""
from collections import deque

n,m,v=map(int,input().split())
graph=[[] for i in range(n+1)]
d_visited=[0]*(n+1)
b_visited=[0]*(n+1)

for i in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(m):
    graph[i].sort()

def dfs(now):
    d_visited[now]=1
    print(now,end=" ")
    for v in graph[now]:
        if d_visited[v]==0:
            dfs(v)

def bfs(now):
    queue=deque([now])
    b_visited[now]=1

    while queue:
        now=queue.popleft()
        print(now,end=" ")
        for v in graph[now]:
            if b_visited[v]==0:
                queue.append(v)
                b_visited[v]=1

dfs(v)
print()
bfs(v)