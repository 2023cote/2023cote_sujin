from itertools import combinations
import sys
input = sys.stdin.readline

N = int(input())
circles = [list(map(int, input().split())) for _ in range(N)]
ans = 'YES'

for two in combinations(circles,2):
  rr=
  dd=
  if abs(two[0][1] + two[1][1]) < abs(two[0][0] - two[1][0]): # 외부
    continue
  elif abs(two[0][1] - two[1][1]) > abs(two[0][0] - two[1][0]): # 내부
    continue
  else:
    ans = 'NO'
    break
print(ans)