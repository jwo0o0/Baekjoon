import sys
import heapq
input = sys.stdin.readline

N = int(input())
h = []
result = []

def maxheap(n):
    if n == 0:
        if len(h) == 0: result.append(0)
        else:
            result.append(-heapq.heappop(h))
    else:
        heapq.heappush(h, -n)


for i in range(N):
    n = int(input())
    maxheap(n)

for i in result:
    print(i)