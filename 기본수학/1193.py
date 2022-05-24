#백준 1193 분수찾기
import sys 
input = sys.stdin.readline 

X = int(input())

def findX(x):
    n = 1
    ans = 0
    i = 0
    while(i < x):
        ans = 0
        for j in range(0, n):
            ans += 1
            i += 1
        for j in range(0, n-1):
            ans -= 1
            i += 1
        n += 2
    return ans

print(findX(X))