"""
문제
일차원 좌표상의 점 N개와 선분 M개가 주어진다. 이때, 각각의 선분 위에 입력으로 주어진 점이 몇 개 있는지 구하는 프로그램을 작성하시오.

입력
첫째 줄에 점의 개수 N과 선분의 개수 M이 주어진다. (1 ≤ N, M ≤ 100,000) 둘째 줄에는 점의 좌표가 주어진다. 두 점이 같은 좌표를 가지는 경우는 없다. 셋째 줄부터 M개의 줄에는 선분의 시작점과 끝점이 주어진다. 입력으로 주어지는 모든 좌표는 1,000,000,000보다 작거나 같은 자연수이다.

출력
입력으로 주어진 각각의 선분 마다, 선분 위에 입력으로 주어진 점이 몇 개 있는지 출력한다.
"""

import sys
input=sys.stdin.readline #이것 안넣으면 error

n,m=map(int,input().split())
dots=sorted(list(map(int,input().split())))

def func(v,dir):
    left,right=0,n-1
    while left<=right:
        mid=(left+right)//2

        if v<dots[mid]:
            right=mid-1
        elif v>dots[mid]:
            left=mid+1
        else:
            return mid
    
    if dir==0:
        return left
    else:
        return right

for _ in range(m):
    start,end=map(int,input().split())
    left,right=func(start,0),func(end,1)
    print(right-left+1)