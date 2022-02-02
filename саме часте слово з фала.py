import reZADACHI
a=str()
b={}
k,v=0,str()
with open ('in.txt') as file_in:
    for i in file_in:
        a=a+i.lower()

result=reZADACHI.findall(r'\w+', a)
for i in result:
    b.setdefault(i,0)
    b[i]+=1
print(b)
for i,j in b.items():
    if k<j:
        k,v=j,i+' '
print(v,k)
with open("out.txt", 'w') as file_out:
    file_out.write(v)
    file_out.write(str(k))