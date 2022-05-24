import sys
from collections import deque
input = sys.stdin.readline
MAX = 100000

N, K = map(int, input().split())

def move(x, i):
    if i == 0: return x+1
    elif i == 1: return x-1
    elif i == 2: return 2*x

dic = {}  
def BFS(start):
    queue = deque([start])
    dic[start] = 0
    if start == K: return 0
    while queue:
        x = queue.popleft()
        for i in range(0, 3):
            dx = move(x, i)
            if 0 <= dx <= MAX and dx not in dic:
                queue.append(dx)
                dic[dx] = 0
                dic[dx] = dic[x] + 1
            if dx == K:
                return dic[K]

print(BFS(N))

'''
실행은 잘 되고 결과값고 맞는데 숫자가 커지면 실행속도가 너무 느려짐
백준에서 채점했을 때는 메모리 초과
-> MAX = 100000, dx 범위 설정해주니 통과
'''



