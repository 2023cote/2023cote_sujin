n,m=map(int,input().split())
mincards=[]
for i in range(n):
    temp=list(map(int,input().split()))
    mincards.append(min(temp))
print(max(mincards))