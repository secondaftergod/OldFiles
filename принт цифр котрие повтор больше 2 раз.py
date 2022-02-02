a=[int(i) for i in input().split()]
b={}

a.sort()
for i in a:
    b.setdefault(i,a.count(i))
c=b.copy()

for i,z in b.items():
   if z==1:
       c.pop(i)

print(*c.keys())
