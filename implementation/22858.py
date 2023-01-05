"""
plst=[0]*n
plst는 for문 안에서 초기화 되어야 한다
"""

n,k=map(int,input().split())
slst=list(map(int,input().split()))
dlst=list(map(int,input().split()))

for i in range(k):
    plst=[0]*n
    for i in range(n):
        plst[dlst[i]-1]=slst[i]
    slst=plst

print(" ".join(map(str,slst)))