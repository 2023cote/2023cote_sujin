"""
문제
정수가 주어지면, 그 수의 정수 제곱근을 구하는 프로그램을 작성하시오.

입력
첫째 줄에 정수 n이 주어진다. (0 ≤ n < 263)

출력
첫째 줄에 q2 ≥ n인 가장 작은 음이 아닌 정수 q를 출력한다.
"""

n=int(input())
s,e=0,n

while s<=e:
    mid=(s+e)//2
    if mid**2<n:
        s=mid+1
    else:
        e=mid-1

print(s)