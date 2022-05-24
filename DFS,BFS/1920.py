import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def binary_search(array, find, start, end):
    mid = (start + end) // 2
    if start > end: return 0
    if array[mid] == find:
        return 1
    elif array[mid] > find:
        return binary_search(array, find, start, mid-1)
    elif array[mid] < find:
        return binary_search(array, find, mid+1, end)


N = int(input())
array = list(map(int, input().split()))
array.sort()

M = int(input())
find = list(map(int, input().split()))

result = []
for i in range(0, M):
    result.append(binary_search(array, find[i], 0, N-1))

#결과 출력
for i in result:
    print(i)

