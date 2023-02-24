n,m,k=map(int,input().split())
nums=list(map(int,input().split()))
nums.sort()

mynums=[nums[-1]]*k+[nums[-2]]

ans=0
while True:
    for mynum in mynums:
        if m==0:
            break
        ans+=mynum
        m-=1
    if m==0:
        break

print(ans)