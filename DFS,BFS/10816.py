import sys
input = sys.stdin.readline

def binary_search(array, find, start, end):
    while start <= end:
        mid = (start+end) // 2
        if array[mid] == find:
            return mid
        elif array[mid] > find:
            end = mid - 1
        else: 
            start = mid + 1
    return None

N = int(input())
array = list(map(int, input().split()))
array.sort()

M = int(input())
find = list(map(int, input().split()))

result = []
for i in range(0, M):
    count = 0
    copied = array.copy()
    r = binary_search(copied, find[i], 0, len(copied)-1)
    while r != None: 
        count += 1
        copied.pop(r)
        r = binary_search(copied, find[i], 0, len(copied)-1)
    result.append(count)

#결과 출력
for i in result:
    print(i, end = ' ')
        
