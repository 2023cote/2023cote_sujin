start=input()
now=ord(start[0])-ord('a'),int(start[1])
dx=[2,2,-2,-2,1,-1,1,-1]
dy=[1,-1,1,-1,2,2,-2,-2]

ans=0
for i in range(8):
    next=now[0]+dx[i],now[1]+dy[i]
    if 1<=next[0]<=8 and 1<=next[1]<=8:
        ans+=1

print(ans)