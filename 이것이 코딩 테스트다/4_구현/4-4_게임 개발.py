n,m=map(int,input().split())
x,y,dir=list(map(int,input().split()))
ans,turned=0,0

#바다=1, 육지=0, 가본육지=-1
maps=[]
for i in range(n):
    maps.append(list(map(int,input().split())))

#북=0, 동=1, 남=2, 서=3
dx=[-1,0,1,0]
dy=[0,1,0,-1]

while True:
    dir-=1
    if dir==-1:
        dir=3

    nx=x+dx[dir]
    ny=y+dy[dir]

    if maps[nx][ny]==0:
        maps[nx][ny]=-1
        x,y=nx,ny
        ans+=1
        turned+=1
        continue
    else:
        turned+=1
    
    if turned==4:
        nx=x-dx[dir]
        ny=y-dy[dir]

        if maps[nx][ny]==0:
            x,y=nx,ny
        else:
            break
        turned=0
