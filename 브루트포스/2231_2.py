N = int(input())

res = 0
for i in range(1, N+1):
    a = list(map(int, str(i))) #map에 int와 list를 넣으면 리스트의 모든 요소를 int를 사용해 변환
    s = i + sum(a)
    if s == N:
        res = i
        break

print(res)
    