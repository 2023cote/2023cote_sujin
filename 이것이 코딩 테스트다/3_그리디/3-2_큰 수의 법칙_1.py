n,m,k=map(int,input().split())
nums=list(map(int,input().split()))
nums.sort()

scnt=m//(k+1)
fcnt=m-scnt

print(nums[-1]*fcnt+nums[-2]*scnt)