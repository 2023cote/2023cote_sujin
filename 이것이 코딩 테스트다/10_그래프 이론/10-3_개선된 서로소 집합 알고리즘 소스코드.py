"""
find_parent 함수는 해당 노드의 루트 노드를 바로 부모 노드로 만든다.
따라서 경로 압축 기법을 이용하게 되면 루트 노드에 더욱 빠르게 접근할 수 있다는 점에서 
기존의 기본적인 알고리즘과 비교했을 때 시간 복잡도가 개선된다
"""
#특정 원소(x)가 속한 집합(루트노드) 찾기
def find_parent(parent,x):
    if parent[x]!=x: #x가 루트노드가 아닌 경우
        parent[x]=find_parent(parent,parent[x])
    return parent[x]

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