from collections import deque

v,e=map(int,input().split())

graph=[[] for _ in range(v+1)] #그래프
indegree=[0]*(v+1) #진입차수

for _ in range(e):
    a,b=map(int,input().split()) #a->b
    graph[a].append(b)
    indegree[b]+=1

#위상정렬 함수
def topology_sort():
    result=[]
    queue=deque()

    #진입차수가 0인 노드를 큐에 삽입
    for i in range(1,v+1):
        if indegree[i]==0:
            queue.append(i)
    
    while queue:
        now=queue.popleft()
        result.append(now)

        for i in graph[now]:
            #해당 원소와 연결된 노드들의 진입차수에서 1 빼기
            indegree[i]-=1

            #새롭게 진입차수가 0이 되는 노드를 큐에 삽입
            if indegree[i]==0:
                queue.append(i)
    
    for i in result:
        print(i,end=" ")

topology_sort()