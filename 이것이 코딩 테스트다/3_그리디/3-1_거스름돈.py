#큰 단위가 작은 단위의 배수인 경우
n=int(input())
cnt=0

coins=[500,100,50,10]

for coin in coins:
    cnt+=n//coin
    n%=coin

print(cnt)