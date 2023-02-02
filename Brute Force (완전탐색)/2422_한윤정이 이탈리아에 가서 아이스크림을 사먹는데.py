"""
문제
한윤정과 친구들은 이탈리아로 방학 여행을 갔다. 이탈리아는 덥다. 윤정이와 친구들은 아이스크림을 사먹기로 했다. 아이스크림 가게에는 N종류의 아이스크림이 있다. 모든 아이스크림은 1부터 N까지 번호가 매겨져있다. 어떤 종류의 아이스크림을 함께먹으면, 맛이 아주 형편없어진다. 따라서 윤정이는 이러한 경우를 피하면서 아이스크림을 3가지 선택하려고 한다. 이때, 선택하는 방법이 몇 가지인지 구하려고 한다.

입력
첫째 줄에 정수 N과 M이 주어진다. N은 아이스크림 종류의 수이고, M은 섞어먹으면 안 되는 조합의 개수이다. 아래 M개의 줄에는 섞어먹으면 안 되는 조합의 번호가 주어진다. 같은 조합은 두 번 이상 나오지 않는다. (1 ≤ N ≤ 200, 0 ≤ M ≤ 10,000)

출력
첫째 줄에, 가능한 방법이 총 몇 개 있는지 출력한다.
"""
import sys
input=sys.stdin.readline

n,m=map(int,input().split())
graph=[[0 for _ in range(n)] for _ in range(n)]

for _ in range(m):
    a,b=map(int,input().split())
    graph[a-1][b-1]=1
    graph[b-1][a-1]=1

res=0
for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            if graph[i][j]==0 and graph[i][k]==0 and graph[j][k]==0:
                res+=1
print(res)