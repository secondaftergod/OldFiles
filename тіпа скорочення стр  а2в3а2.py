a=input()
z=0
s=0
while z!=len(a):
    j=0 #кількість букв
    while a[z]==a[s]:
        j+=1
        s+=1
        if s>=len(a):
            break
    print(a[z],j,sep='',end='')
    z=s


