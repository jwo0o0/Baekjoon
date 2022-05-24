# -*- coding: utf-8 -*-

N, M = input().split()
N = int(N)
M = int(M)

cards = list(map(int, input().split()))
cards.sort()

sum = 0
diff = M
for i in range(0, N-2):
    tmp = 0
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            tmp = cards[i] + cards[j] + cards[k]
            if diff > M - tmp and M - tmp >= 0: 
                diff = M - tmp
                sum = tmp

print(sum)
