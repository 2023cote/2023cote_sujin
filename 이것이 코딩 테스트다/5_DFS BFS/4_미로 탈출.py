from collections import deque
n,m=map(int,input().split())
graph=[]
for _ in range(n):
    graph.append(list(map(int,input())))

#상하좌우
dy=[-1,1,0,0]
dx=[0,0,-1,1]

def bfs(x,y):
    queue=deque([(x,y)])

    while queue:
        x,y=queue.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]

            if nx<0 or nx>=n or ny<0 or ny>=m:
                continue
            
            #해당 노드를 처음 방문하는 경우에만 최단거리 갱신
            if graph[nx][ny]==1:
                graph[nx][ny]=graph[x][y]+1
                queue.append((nx,ny))
            else:
                continue
    return graph[n-1][m-1]

print(bfs(0,0))