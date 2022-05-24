import sys
input = sys.stdin.readline

# 감염된 컴퓨터의 수
count = 0

def DFS(graph, v, visited):
    global count
    visited[v] = True
    for i in graph[v]:
        if visited[i] == False:
            count += 1
            DFS(graph, i, visited)

N = int(input()) #컴퓨터의 수
link = int(input())

#컴퓨터가 연결된 네트워크 정보
graph = []
for i in range(0, N+1):
    empty = []
    graph.append(empty)

for i in range(0, link):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (N+1)
DFS(graph, 1, visited)

print(count)