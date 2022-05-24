import sys
from collections import deque
input = sys.stdin.readline

miro = []
#N, M 입력 받기
N, M = map(int, input().split())

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
#BFS 탐색 함수
def BFS(n, m):
    queue = deque([(n, m)])
    while queue:
        a, b = queue.popleft()
        for i in range(0, 4):
            da = a+dx[i]
            db = b+dy[i]
            if da < 0 or da > N or db < 0 or db > M:  #미로를 벗어나면 안됨
                continue
            if miro[da][db] == 0: #0인 경우 통과 못함
                continue           
            if miro[da][db] == 1:
                miro[da][db] = miro[a][b] + 1
                queue.append((da, db))
    return miro[N][M]

#미로 입력 받기
miro.append([0]* (M+1))
for i in range(1, N+1):
    miro.append([0])
    n = input()
    for j in range(0, M):
        miro[i].append(int(n[j]))

print(BFS(1, 1))