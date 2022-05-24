#내맘대로 버전 -> 시간초과
import sys
input = sys.stdin.readline

K, N = map(int, input().split())
YS = []
for i in range(0, K):
    YS.append(int(input()))

count = 10**6
i = 1
tmp = 0
while True:
    #print(i)
    for j in range(0, K):
        #print(YS[j] // i, end = ' ')
        tmp += (YS[j] // i)
    #print()
    if tmp < N:
        break
    i += 1
    tmp = 0

print(i-1)