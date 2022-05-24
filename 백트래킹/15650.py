import sys
input = sys.stdin.readline

N, M = map(int, input().split())

result = []
visited = [False] * (N+1)
def recur(num, count):
    if count == M:
        print(' '.join(map(str, result)))
        return 
    for i in range(num+1, N+1):
        result.append(i)
        visited[i] = True
        recur(i, count+1)
        visited[i] = False
        result.pop()

recur(0, 0)