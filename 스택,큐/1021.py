import sys
from collections import deque

queue = deque()
tmp = deque()

N, M = input().split()
N = int(N)
M = int(M)

for i in range(1, N+1):
    queue.append(i)

#뽑아내려는 수들
num = sys.stdin.readline().split()
num = list(map(int, num))

sum = 0 #2번 3번 연산의 수행횟수

for i in range(0, M):
    while queue[0] != num[i]:
        #2번 연산
        if queue.index(num[i]) <= len(queue) - queue.index(num[i]) - 1:
            queue.append(queue[0])
            queue.popleft()
            sum += 1
        else:  # 3번 연산
            tmp = queue.copy()
            queue[0] = tmp[-1]
            for j in range(1, len(queue)):
                queue[j] = tmp[j-1]
            sum += 1
    queue.popleft() #1번 연산

print(sum)
            


