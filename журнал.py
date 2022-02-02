import reZADACHI
a=[]
fa={}
with open('in.txt') as file_in:
    for i in file_in:
        a.append(reZADACHI.findall(r'\w+', i))
for i in range(len(a)):
    fa.setdefault(a[i][0], a[i][1:])

def gurnal(fam,ocinku):
    mat=0
    fiz=0
    rus=0
    with open("out.txt", 'w') as file_out:
        for i in list(ocinku):
            mat=mat+int(i[0])
            fiz=fiz+int(i[1])
            rus=rus+int(i[2])
            file_out.write(str((int(i[0])+int(i[1])+int(i[2]))/3)+'\n')
        file_out.write(str(mat/len(ocinku))+' '+str(fiz/len(ocinku))+' '+str(rus/len(ocinku)))

gurnal(fa.keys(),fa.values())


