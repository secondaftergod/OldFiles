n=int(input())
z=[]
x=[i for i in range(n+1)]
a=[[i for j in range(x[i])]for i in range(len(x))]
for i in a:
    for j in i:
        z.append(j)

print(*z[0:n])
