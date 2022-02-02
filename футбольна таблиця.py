import reZADACHI
igr=int(input())
tab={}
for i in range(igr):
	igra=input()
	kmd=reZADACHI.split(r'[;]', igra)
	del kmd[1], kmd[2]
	for i in range(len(kmd)):
		tab.setdefault(kmd[i],[0,0,0,0,0])
		rez=reZADACHI.findall(r'\d+', igra)
		if int(rez[i])>int(rez[i-1]):
			tab[kmd[i]][1]+=1
			tab[kmd[i]][4]+=3
		elif int(rez[i])<int(rez[i-1]):
			tab[kmd[i]][3]+=1
		elif int(rez[i])==int(rez[i-1]):
			tab[kmd[i]][2]+=1
			tab[kmd[i]][4]+=1
		tab[kmd[i]][0]+=1
for i,j in tab.items():
    print((i+':{} {} {} {} {}').format(*j))





