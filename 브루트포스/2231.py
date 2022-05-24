N = int(input())

ans = 0
for i in range(1, N+1):
    sum = i
    cnt = i
    while cnt >0:
        sum += cnt%10
        cnt = cnt//10
    print(sum)
    if sum == N:
        ans = sum
        break

print(ans)
