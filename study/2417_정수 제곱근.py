"""
문제
정수가 주어지면, 그 수의 정수 제곱근을 구하는 프로그램을 작성하시오.

입력
첫째 줄에 정수 n이 주어진다. (0 ≤ n < 263)

출력
첫째 줄에 q2 ≥ n인 가장 작은 음이 아닌 정수 q를 출력한다.
"""

n=int(input())
tests=[i for i in range(1,n+1)]

def func(x):
    s,e=0,n-1
    while s<=e:
        mid=(s+e)//2
        if n<tests[mid]**2:
            e=mid-1
        elif n>tests[mid]**2:
            s=mid+1
        else:
            return 1
    return 0

for test in tests:
    print(func(test))
