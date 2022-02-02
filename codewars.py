
def find_outlier(integers):
	k1=0
	k2=0
	for i in range(0,3):
		if integers[i]%2==0:
			k1+=1
		elif integers[i]%2==1:
			k2+=1
	if k1>k2:
		for i in integers:
			if i%2==1:
				return i
	elif k2>k1:
		for i in integers:
			if i%2==0:
				return i

print(find_outlier([160, 3, 1719, 19, 11, 13, -21]))

