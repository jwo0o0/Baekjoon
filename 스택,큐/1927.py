import sys
import heapq
input = sys.stdin.readline


N = int(input())
h = []
result = []

#최소 힙
def heapsort(n):
    if n == 0:
        if len(h) == 0: result.append(0)
        else: result.append(heapq.heappop(h))
    else: 
        heapq.heappush(h, n)

#입력
for i in range(N):
    n = int(input())
    heapsort(n)

for i in result:
    print(i)




