# N과 M (4)
import sys 
input = sys.stdin.readline 

N, M = map(int, input().split())

result = []
def recur(num, cnt):
    if cnt == M:
        print(' '.join(map(str, result)))
        return
    for i in range(num, N+1):
        result.append(i)
        recur(i, cnt+1)
        result.pop()

recur(1, 0)