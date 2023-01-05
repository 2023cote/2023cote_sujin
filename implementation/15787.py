n,m=map(int,input().split())
trains=[[0]*21]*(n+1)
memories=[]
cnt=0
for i in range(m):
    cmd=list(map(int,input().split()))
    if len(cmd)==3:
        a,b,c=cmd[0],cmd[1],cmd[2]
    else:
        a,b=cmd[0],cmd[1]
    if a==1:
        trains[b][c]=1
    elif a==2:
        trains[b][c]=0
    elif a==3:
        trains[b][2:20]=trains[b][1:19]
        trains[b][1]=0
    elif a==4:
        trains[b][1:19]=trains[b][2:20]
        trains[b][20]=0
    else:
        print("wrong input")
    
    if trains[b] not in memories:
        memories.append(trains[b])
        cnt+=1

print(cnt)