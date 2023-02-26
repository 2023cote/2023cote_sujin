def find_parent(parent,x):
    if parent[x]!=x:
        parent[x]=find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,a,b):
    A=find_parent(parent,a)
    B=find_parent(parent,b)

    if A<B:
        parent[B]=A
    else:
        parent[A]=B

v,e=map(int,input().split())
parent=[i for i in range(v+1)]

cycle=False #사이클 발생 여부

for i in range(e):
    a,b=map(int,input().split())

    if find_parent(parent,a)==find_parent(parent,b):
        cycle=True
        break
    else:
        union_parent(parent,a,b)

if cycle:
    print("사이클이 발생했습니다")
else:
    print("사이클 없습니다")