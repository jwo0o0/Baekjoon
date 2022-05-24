import sys
input = sys.stdin.readline

N = int(input())
sum = 0
result = [] #결과 입력받을 배열

graph = []
for i in range(N):
    graph.append([])

#지도 입력받기
for i in range(N):
    n = str(input())
    for j in range(N):
        graph[i].append(n[j])

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def DFS(x, y):
    global sum
    #단지 밖으로 나가는 경우
    if x < 0 or x >= N or y < 0 or y >= N: #여기서 범위 잘 설정해줘야 함!
        return False
    if graph[x][y] == '1':
        sum += 1
        graph[x][y] = '0' #방문한 곳은 0으로 바꿔줌
        for i in range(4): #양방향으로 이동
            DFS(x+dx[i], y+dy[i])
        return True
    return False

for i in range(N):
    for j in range(N):
        if DFS(i, j) == True:
            result.append(sum)
            sum = 0

print(len(result))
result.sort()
for i in result:
    print(i)