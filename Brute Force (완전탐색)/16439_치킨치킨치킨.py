"""
문제
N명의 고리 회원들은 치킨을 주문하고자 합니다.

치킨은 총 M가지 종류가 있고 회원마다 특정 치킨의 선호도가 있습니다. 한 사람의 만족도는 시킨 치킨 중에서 선호도가 가장 큰 값으로 결정됩니다. 진수는 회원들의 만족도의 합이 최대가 되도록 치킨을 주문하고자 합니다.

시키는 치킨의 종류가 많아질수록 치킨을 튀기는 데에 걸리는 시간도 길어지기 때문에 최대 세 가지 종류의 치킨만 시키고자 합니다.

진수를 도와 가능한 만족도의 합의 최댓값을 구해주세요.

입력
첫 번째 줄에 고리 회원의 수 N (1 ≤ N ≤ 30) 과 치킨 종류의 수 M (3 ≤ M ≤ 30) 이 주어집니다.

두 번째 줄부터 N개의 줄에 각 회원의 치킨 선호도가 주어집니다.

i+1번째 줄에는 i번째 회원의 선호도 ai,1, ai,2, ..., ai,M (1 ≤ ai,j ≤ 9) 가 주어집니다.

출력
첫 번째 줄에 고리 회원들의 만족도의 합의 최댓값을 출력합니다.
"""
from itertools import combinations 
#itertools 사용하는 것 보다 3중 반복문 사용하는게 더 짧게 걸림
n,m=map(int,input().split())
prefers=[]
for _ in range(n):
    prefers.append(list(map(int,input().split())))

res=0
for chicken in combinations(range(m),3):
    now=0
    for i in range(n):
        now+=max(prefers[i][chicken[0]],prefers[i][chicken[1]],prefers[i][chicken[2]])
    if res<now:
        res=now

print(res)