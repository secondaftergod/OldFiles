bag={'rope':1,'dagger':2,'arrow':20}
loot=['arrow','dagger','coin','coin','gops','arrow','rope']
def add(inv,addloot):
	for i in addloot:
		if inv.get(i)==None:
			inv[i]=1
		else:
			inv[i]+=1
		
def bags(items):
	add(bag,loot)
	total=0
	for i,z in bag.items():
		print(i+' '+str(z))
		total+=z
	print('Total'+' '+str(total))
bags(bag)
		
	


