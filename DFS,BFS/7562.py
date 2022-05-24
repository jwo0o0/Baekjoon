import sys
from collections import deque
input = sys.stdin.readline

dy = [-1, -2, -2, -1, 1, 2, 2, 1]
dx = [-2, -1, 1, 2, 2, 1, -1, -2]
#BFS로 탐색
def BFS(y, x, des_y, des_x):
    queue = deque([(y, x)])
    if y == des_y and x == des_x: #출발지와 목적지가 같을 경우 바로 리턴
        return
    while queue:
        vy, vx = queue.popleft()
        for i in range(0, 8):
            ny = vy+dy[i]
            nx = vx+dx[i]
            if ny < 0 or ny >= l or nx < 0 or nx >= l: #체스판을 벗어나는 경우
                continue 
            if Chess[ny][nx] == 0: #방문하지 않은 경우
                Chess[ny][nx] = Chess[vy][vx] + 1
                queue.append((ny, nx))
            if ny == des_y and nx == des_x: #목적지인 경우 리턴
                return

result = []
N = int(input())

for n in range(0, N):
    l = int(input())
    Chess = []
    for i in range(0, l): #체스판 생성
        Chess.append([])
        for j in range(0, l):
            Chess[i].append(0)

    start_y, start_x = map(int, input().split())
    des_y, des_x = map(int, input().split())

    BFS(start_y, start_x, des_y, des_x)
    result.append(Chess[des_y][des_x])

for i in result:
    print(i)