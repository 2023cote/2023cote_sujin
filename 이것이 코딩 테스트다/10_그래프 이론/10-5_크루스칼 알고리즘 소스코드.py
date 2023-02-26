"""
최소 비용 신장 트리를 만드는데 필요한 비용을 계산
union find
무방향 그래프의 사이클 형성여부 체크
크루스칼
"""
def find_parent(parent,x):
    if parent[x]!=x:
        parent[x]=find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,a,b):
    pa=find_parent(parent,a)
    pb=find_parent(parent,b)
    if a<b:
        parent[b]=a
    else:
        parent[a]=b

v,e=map(int,input().split())
parent=[i for i in range(v+1)]

#모든 간선에 대한 정보 입력받기
edges=[]
for _ in range(e):
    a,b,cost=map(int,input().split())
    edges.append((cost,a,b))

#간선을 비용순으로 정렬
edges.sort() #edges.sort(key=lambda x:x[0])

#최송비용 신장트리의 가중치를 계산하기 위해
res=0
#간선을 하나씩 확인하며
for edge in edges:
    cost,a,b=edge

    #사이클이 발생하지 않는 경우에만
    if find_parent(parent,a)!=find_parent(parent,b):
        union_parent(parent,a,b) #집합에 포함
        res+=1

print(res)