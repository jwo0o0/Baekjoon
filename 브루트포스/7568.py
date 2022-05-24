N = int(input())

kg = list()
cm = list()
for i in range(0, N):
    x, y = input().split()
    kg.append(int(x))
    cm.append(int(y))

#rank list 생성
rank = list()
for i in range(0, N):
    rank.append(1)
#덩치 계산
for i in range(0, N):
    for j in range(0, N):
        if kg[j] > kg[i] and cm[j] > cm[i]:
            rank[i] += 1
#출력
for i in rank:
    print(i, end=' ')
        
