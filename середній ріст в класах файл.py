import reZADACHI
count={}
rez=[]
a=0
with open ('in.txt') as file_in:
    for i in file_in:
        rez.append(reZADACHI.findall(r'\d+', i))
sp={x: 0 for x in range(1, 12)}
for i in range(len(rez)):
    count.setdefault(int(rez[i][0]),0)
    count[int(rez[i][0])]+=1
for i in range(len(rez)):
    sp[int(rez[i][0])]+=int(rez[i][1])/count[int(rez[i][0])]
for i,j in sp.items():
    if j==0:
        sp[i]='-'
for i, j in sp.items():
    print(i,j)
with open("out.txt", 'w') as file_out:
    for i, j in sp.items():
        file_out.write(str(i)+' '+str(j)+'\n')

