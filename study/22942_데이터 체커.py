"""
문제
원 이동하기 2 문제를 만들고 만든 데이터가 문제의 조건에 맞는지 확인하는 코드를 작성해야한다.

해당 문제의 데이터는 아래 조건들을 만족해야한다.

모든 원의 중심 좌표는 
$x$축 위에 존재해야 한다.
 
$N$개의 원 중 임의의 두 원을 선택했을 때, 교점이 존재하지 않아야 한다. 즉, 하나의 원이 다른 원 안에 존재하거나 외부에 존재한다.
데이터 형식은 원의 개수 
$N$이랑 각 원의 중심 
$x$좌표, 원의 반지름 
$r$만 주어진다. 따라서, 2번 조건을 만족하는지만 확인하면 된다.

주어진 데이터가 해당 조건을 만족하는지 확인해보자.

입력
첫 번째 줄에는 원의 개수 
$N$이 주어진다.

두 번째 줄부터 
$N+1$번째 줄까지 원의 중심 
$x$좌표, 원의 반지름 
$r$이 공백으로 구분되어 주어진다.

출력
데이터가 조건에 맞는다면 YES, 조건에 만족하지 않는다면 NO를 출력한다.
"""
import sys
input=sys.stdin.readline

n=int(input())
circles=[]
stack=[]

for i in range(n):
    x,r=map(int,input().split()) #원의 중심, 원의 반지름
    circles.append([x-r,i,0]) #좌표 원이름 시작점
    circles.append([x+r,i,1]) #좌표 원이름 끝점

circles.sort()

for i in range(n):
    now=circles[i]

    if now[2]==0: #열림
        stack.append(circles[i])
    else: #닫힘
        before=stack[-1]
        
        if before[2]==0:
            if now[1]==before[1]:
                stack.pop()
            else:
                print("NO")
                exit(0)

print("YES")
