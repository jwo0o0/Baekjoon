import sys
from collections import deque

d = deque()

N = int(sys.stdin.readline())

for i in range(0, N):
    order = sys.stdin.readline().split()
    if order[0] == 'push_front':
        d.appendleft(order[1])
    elif order[0] == 'push_back':
        d.append(int(order[1]))
    elif order[0] == 'pop_front':
        if len(d) == 0: print(-1)
        else: 
            print(d.popleft())
    elif order[0] == 'pop_back':
        if len(d) == 0: print(-1)
        else:
            print(d.pop())
    elif order[0] == 'size':
        print(len(d))
    elif order[0] == 'empty':
        if d: print(0)
        else: print(1)
    elif order[0] == 'front':
        if len(d) != 0: print(d[0])
        else: print(-1)
    elif order[0] == 'back':
        if len(d) != 0: print(d[-1])
        else: print(-1)