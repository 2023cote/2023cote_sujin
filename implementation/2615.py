import sys
input = sys.stdin.readline

# 0으로 이루어진 패딩 추가
board = [[0]*21] + [[0]+list(map(int,input().split()))+[0] for _ in range(19)] + [[0]*21]
move = [(0,1),(1,0),(1,1),(-1,1)]
for i in range(1,20):
    for j in range(1,20):
        if board[i][j] != 0:
            for a,b in move:
                if i+a*4>=20 or j+b*4>=20 or 1>i+a*4 or 1>j+b*4:
                    continue
                line = [board[i+a*k][j+b*k] for k in range(-1,6)]
                # 가운데 부분, 앞과 뒤 5개씩 끊어서 확인
                if len(set(line[1:6])) == 1 and len(set(line[0:5])) == 2 and len(set(line[1:7]))==2:
                    print(board[i][j])
                    print(i,j)
                    sys.exit()
print(0)