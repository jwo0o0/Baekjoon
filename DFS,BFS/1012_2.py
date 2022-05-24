#BFS
import sys
from collections import deque

T = int(input())
result = []
bat = []
sum = 0

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
def BFS(y, x):
    queue = deque([(y, x)])
    bat[y][x] = 0
    while queue:
        b, a = queue.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if nx < 0 or nx >= M or ny < 0 or ny >= N:
                continue
            if bat[ny][nx] == 1:
                bat[ny][nx] = 0
                queue.append((ny, nx))

for t in range(0, T):
    M, N, K = map(int, sys.stdin.readline().split())

    #밭 입력 받기
    bat = []
    for i in range(0, N):
        bat.append([])
        for j in range(0, M):
            bat[i].append(0)

    for i in range(0, K): #K번 입력 받기
        x, y = map(int, sys.stdin.readline().split())
        bat[y][x] = 1

    count = 0
    for i in range(0, M):
        for j in range(0, N):
            if bat[j][i] == 1:
                BFS(j, i)
                count += 1

    result.append(count)

#결과 출력
for i in result:
    print(i)
