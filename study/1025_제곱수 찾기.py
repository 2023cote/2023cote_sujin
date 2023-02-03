"""
문제
N행 M열의 표 A가 있고, 표의 각 칸에는 숫자가 하나씩 적혀있다.

연두는 서로 다른 1개 이상의 칸을 선택하려고 하는데, 행의 번호가 선택한 순서대로 등차수열을 이루고 있어야 하고, 열의 번호도 선택한 순서대로 등차수열을 이루고 있어야 한다. 이렇게 선택한 칸에 적힌 수를 순서대로 이어붙이면 정수를 하나 만들 수 있다.

연두가 만들 수 있는 정수 중에서 가장 큰 완전 제곱수를 구해보자. 완전 제곱수란 어떤 정수를 제곱한 수이다.

입력
첫째 줄에 N, M이 주어진다. 둘째 줄부터 N개의 줄에는 표에 적힌 숫자가 1번 행부터 N번 행까지 순서대로 한 줄에 한 행씩 주어진다. 한 행에 적힌 숫자는 1번 열부터 M번 열까지 순서대로 주어지고, 공백없이 모두 붙여져 있다.

출력
첫째 줄에 연두가 만들 수 있는 가장 큰 완전 제곱수를 출력한다. 만약, 완전 제곱수를 만들 수 없는 경우에는 -1을 출력한다.

제한
1 ≤ N, M ≤ 9
표에 적힌 숫자는 0보다 크거나 같고, 9보다 작거나 같다.
"""
from math import sqrt

n,m=map(int,input().split())
graph=[]
for _ in range(n):
    graph.append(list(input()))


def isSquare(p):
    p=int(p)
    return int(p**0.5)**2==p

res=-1
for i in range(n):
    for j in range(m):
        for row_distance in range(-n,n):
            for col_distance in range(-m,m):
                num=''
                x=i
                y=j

                if row_distance==0 and col_distance==0:
                    continue

                while 0<=x<n and 0<=y<m:
                    num+=graph[x][y]
                    if isSquare(num):
                        res=max(res,int(num))
                    x+=row_distance
                    y+=col_distance

print(res)