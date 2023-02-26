"""
1을 만들기 위해 사용할 수 있는 연산
1. 5로 나누기 (5로 나누어 떨어지는 경우)
2. 3으로 나누기 (3로 나누어 떨어지는 경우)
3. 2로 나누기 (2로 나누어 떨어지는 경우)
4. 1을 빼기
"""

x=int(input())
dp=[0]*30001

for i in range(2,x+1):
    dp[i]=dp[i-1]+1

    if i%5==0:
        dp[i]=min(dp[i],dp[i//5]+1)
    if i%3==0:
        dp[i]=min(dp[i],dp[i//3]+1)
    if i%2==0:
        dp[i]=min(dp[i],dp[i//2]+1)

print(dp[x])
