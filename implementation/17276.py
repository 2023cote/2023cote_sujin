t=int(input())
for i in range(t):
    n,d=map(int,input().split())

    while d<0 or d>=360:
        if d<0:
            d+=360
        if d>=360:
            d-=360
    lst=[]
    ulst=[]
    dlst=[]
    hlst=[]
    vlst=[]
    center=n//2

    for i in range(d//45):
        for i in range(n):
            lst.append(list(map(int,input().split())))
            ulst.append(lst[i][n-1-i])
            dlst.append(lst[i][i])
            vlst.append(lst[i][center])
        hlst.append(lst[center])

        ulst,dlst,hlst,vlst=vlst,hlst,ulst,dlst
        for i in range(n):
            lst[i][n-1-i]=ulst[i]
            lst[i][i]=dlst[i]
            lst[i][center]=vlst[i]
        lst[center]=hlst
        print(lst)