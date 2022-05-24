from collections import deque
import sys


N, M, V = map(int, sys.stdin.readline().split())

#그래프 생성
graph = []
for i in range(N+1):
    line = []
    graph.append(line)

#간선 입력
for i in range(0, M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
  
#입력 후 정렬
for k in graph:
    k.sort()

def DFS(v):
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            DFS(i)

def BFS(start):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

#방문했는지 확인할 리스트
visited = [False] * (N+1)
DFS(V)

print()
visited = [False] * (N+1)
BFS(V)


