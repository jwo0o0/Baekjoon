#이진탐색으로
import sys
input = sys.stdin.readline

K, N = map(int, input().split())
YS = []
for i in range(0, K):
    YS.append(int(input()))

start = 1
#end = 2**31 - 1 이 아님
end = max(YS)

#이진탐색
while start <= end:
    mid = (start + end) // 2
    tmp = 0
    for i in YS:
        tmp += i // mid
    if tmp >= N:
        start = mid + 1     
    else:
        end = mid - 1

#print(mid)가 아님
print(end)