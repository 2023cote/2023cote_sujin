n=int(input())
plans=input().split()

x,y=1,1
dx=[0,0,-1,1]
dy=[-1,1,0,0]
moves=['L','R','U','D']

for plan in plans:
    for i in range(4):
        if plan==moves[i]:
            nx=x+dx[i]
            ny=y+dy[i]
    if nx<1 or nx>n or ny<1 or ny>n:
        continue
    else:
        x,y=nx,ny

print(x,y)
