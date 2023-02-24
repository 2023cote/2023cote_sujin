n=int(input())
now=""
res=0
for i in range(n+1):
    for j in range(60):
        for k in range(60):
            now=str(i)+str(j)+str(k)
            if '3' in now:
                res+=1

print(res)