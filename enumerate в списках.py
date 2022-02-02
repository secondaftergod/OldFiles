x=[int(i) for i in input().split()]
n=int(input())
if x.count(n)==0:
    print('Отсутствует')
for i,j in enumerate(x):
    if j==n:
        print(i,end=' ')


