s='shdahf'
a=s.find('h')
b=s.rfind('h')
c=s[s.find('h')+1:s.rfind('h')]
print(c)
print(s[:a],c[::-1],s[b+1:],sep='')
