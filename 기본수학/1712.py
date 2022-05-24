import sys
input = sys.stdin.readline

A, B, C = map(int, input().split())

def year(n):
    global A, B
    return A + B * n

if B >= C:
    print(-1)
else:
    print(A // (C-B)+1)
