import reZADACHI
shufr={}
sl=input()
kod=input()
usl1=input()
usl2=input()

sl_list=reZADACHI.findall(r'.', sl)
kod_list=reZADACHI.findall(r'.', kod)
for i in range(len(sl_list)):
	shufr.setdefault(sl_list[i],kod[i])
shufr_ob={v: k for k,v in shufr.items()}
for i in usl1:
	print(shufr[i],end='')
print('')
for i in usl2:
	print((shufr_ob[i]),end='')
