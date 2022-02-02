a = int(input())
b = int(input())
c = int(input())
d = int(input())
for z in range(c,d+1):
    print('\t','\t',z,end='\t')
print(end='\n')

for i in range(a, b + 1):
    print(i,end='\t')
    for j in range(c, d + 1):
        g = i * j
        print('\t',g, end='\t')
    print(end='\n')
