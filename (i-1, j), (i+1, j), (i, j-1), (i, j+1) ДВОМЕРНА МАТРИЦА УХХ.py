import copy

a=[]
c=[]
k=0

while True:
    sek=input().split()
    try:
        sek.index('end')
    except ValueError:
        for i in range(len(sek)):
            sek[i]=int(sek[i])
        a.append(sek)
        k+=1
        continue
    break

b=copy.deepcopy(a)


def zag():  # якщо len(a)!=1
    for i in range(-1, len(a)-1):
        for j in range(-1, len(a[i])-1):
            b[i][j]=a[i-1][j]+a[i+1][j]+a[i][j-1]+a[i][j+1]
    for l in b:
        print(*l)


def t(m):  # транспортація рядок в стовбці
    return [list(x) for x in zip(*m)]


def k(a):  # якщо len(a)<=1
    for i in range(len(a)):
        c.append(a[i]*3)
    g=copy.deepcopy(c)
    for i in range(-1, len(c)-1):
        for j in range(-1, len(c[i])-1):
            g[i][j]=c[i-1][j]+c[i+1][j]+c[i][j-1]+c[i][j+1]
    return g


if len(a) <= 1:
    if len(a[0]) == 1:
        for z in a:
            for i in range(len(z)):
                if i < len(z)-1:
                    c.append(z[i+1]+z[i-1]+z[0]+z[0])
                else:
                    c.append(z[0]+z[i-1]+z[0]+z[0])
        print(*c)
    else:
        for z in k(t(a)):
            print(z[0], end=' ')

elif len(a) > 1:
    if len(a[0]) != 1:
        zag()
    else:
        for z in k(a):
            print(z[0])
