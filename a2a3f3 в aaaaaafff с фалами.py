import reZADACHI
a=str()
with open ('in.txt') as file_in:
    for line in file_in:
        line=line.strip()
        x=line
result1=reZADACHI.findall(r'\d+', x)
result2=[]
for i in x:
    if i.isalpha()==True:
        result2.append(i)
for i in range(len(result2)):
    a=a+str(result2[i]*int(result1[i]))
with open("out.txt", 'w') as file_out:
    file_out.write(a)