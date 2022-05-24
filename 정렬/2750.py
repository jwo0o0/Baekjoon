N = int(input())

array = []
for i in range(0, N):
    n = int(input())
    array.append(n)

array.sort()

#출력
for i in array:
    print(i)
