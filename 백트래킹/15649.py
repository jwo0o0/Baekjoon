import sys
input = sys.stdin.readline

N, M = map(int, input().split())

result = []
visited = [False] * (N+1)

def recur(num):
    if num == M:
        print(' '.join(map(str, result)))
        return
    for i in range(1, N+1): 
        if visited[i] == False:
            visited[i] = True
            result.append(i)
            recur(num+1)
            visited[i] = False #빼주는 부분 필요함
            result.pop()

recur(0)


"""
1. 아이디어
- 백트래킹, 재귀함수
2. 시간복잡도
- N! > 가능
3. 자료구조
- 결과값 저장 int[]
- 방문여부 체크 bool[]
"""