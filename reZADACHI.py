s='ababc'
a='c'
b='c'
class Changes(str):
	def replace(self,sho,nasho,de):
		k=0
		#super().replace(sho,nasho)
		while sho in de:
			de=de.replace(sho,nasho)
			k+=1
			if k>=1000:
				print('Impossible')
				break
		if k!=1000:
			print(k)
o=Changes()
#o.replace(a,b,s)
"""----------------------------------------"""
s='abababa'
t='aba'
count=0
for i in range(len(s)):
	if s[i:].startswith(t):
		count+=1
#print(count)
"""----------------------------------------"""
import reZADACHI
s, t = s, '(?=' +t + ')'
#print(len(re.findall(t, s)))
"""----------------------------------------"""



import reZADACHI
k='catcat'
v=reZADACHI.findall(r'cat', k)
if len(v)>=2:
	print(k)

