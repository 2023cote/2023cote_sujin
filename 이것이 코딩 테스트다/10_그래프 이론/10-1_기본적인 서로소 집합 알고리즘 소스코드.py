#특정 원소(x)가 속한 집합(루트노드) 찾기
def find_parent(parent,x):
    if parent[x]!=x: #x가 루트노드가 아닌 경우
        return find_parent(parent,parent[x])
    else:
        return x

#두 원소가 속한 집합(루트노드) 합치기
def union_parent(parent,a,b):
    A=find_parent(parent,a) #a의 루트노드 A
    B=find_parent(parent,b) #b의 루트노드 B

    if A<B:
        parent[B]=A
    else:
        parent[A]=B

v,e=map(int,input().split()) #노드개수, 간선개수
parent=[i for i in range(v+1)] #부모 테이블을 자기 자신으로 초기화

#union 연산 수행
for i in range(e):
    a,b=map(int,input().split())
    union_parent(parent,a,b)

for i in range(1,v+1):
    print(find_parent(parent,i),end=" ")
print()
for i in range(1,v+1):
    print(parent[i],end=" ")