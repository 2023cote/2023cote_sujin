"""
문제
N×M크기의 배열로 표현되는 미로가 있다.

1	0	1	1	1	1
1	0	1	0	1	0
1	0	1	0	1	1
1	1	1	0	1	1
미로에서 1은 이동할 수 있는 칸을 나타내고, 0은 이동할 수 없는 칸을 나타낸다. 이러한 미로가 주어졌을 때, (1, 1)에서 출발하여 (N, M)의 위치로 이동할 때 지나야 하는 최소의 칸 수를 구하는 프로그램을 작성하시오. 한 칸에서 다른 칸으로 이동할 때, 서로 인접한 칸으로만 이동할 수 있다.

위의 예에서는 15칸을 지나야 (N, M)의 위치로 이동할 수 있다. 칸을 셀 때에는 시작 위치와 도착 위치도 포함한다.

입력
첫째 줄에 두 정수 N, M(2 ≤ N, M ≤ 100)이 주어진다. 다음 N개의 줄에는 M개의 정수로 미로가 주어진다. 각각의 수들은 붙어서 입력으로 주어진다.

출력
첫째 줄에 지나야 하는 최소의 칸 수를 출력한다. 항상 도착위치로 이동할 수 있는 경우만 입력으로 주어진다.
"""
"""
import sys
sys.setrecursionlimit 안넣으면 런타임에러 발생
"""
import sys
from collections import deque
sys.setrecursionlimit(10**6)
input=sys.stdin.readline

n,m=map(int,input().split())
graph= [list(map(int,list(input().rstrip()))) for i in range(n)]
visited=[[0 for i in range(m)] for i in range(n)]
visited[0][0]=1

move=[[-1,0],[1,0],[0,-1],[0,1]] #상하좌우 탐색
queue=deque()

def bfs(point):
    for i in move:
        x,y=point[0]+i[0],point[1]+i[1]
        # 인덱스를 초과하지 않으며, 경로가 존재하고, 방문하지 않은 지점일 경우
        while 0<=x<n and 0<=y<m and graph[x][y]==1 and visited[x][y]==0:
            queue.append((x,y))
            visited[x][y]=1
            graph[x][y]+=graph[point[0]][point[1]]
    
    if queue:
        bfs(queue.popleft())

bfs((0,0))
print(graph[n-1][m-1])