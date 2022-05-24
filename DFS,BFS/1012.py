#DFS
import sys
sys.setrecursionlimit(10**6)

T = int(input())
result = []
sum = 0

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
def DFS(y, x):
    global sum
    if x < 0 or x >= M or y < 0 or y >= N:
        return False
    if bat[y][x] == 0: return False
    if bat[y][x] == 1:
        sum += 1
        bat[y][x] = 0
        for i in range(0, 4):
            DFS(y+dy[i], x+dx[i])
        return True
    return False
    
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
            if DFS(j, i) == True:
                count += 1

    result.append(count)

#결과 출력
for i in result:
    print(i)
