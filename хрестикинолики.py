xo={'1':' ','2':' ','3':' ','4':' ','5':' ',
	'6':' ','7':' ','8':' ','9':' '}
	
def printxo(board):
	print('#######')
	print('#'+board['1']+'|'+board['2']+'|'+board['3']+'#')
	print('#-+-+-#')
	print('#'+board['4']+'|'+board['5']+'|'+board['6']+'#')
	print('#-+-+-#')
	print('#'+board['7']+'|'+board['8']+'|'+board['9']+'#')
	print('#######')

def comp(igra):
	if igra['5']==' ':
		igra['5']='O'
	if igra['5']=='X':
		igra['1']='O'
	if igra['5']+igra['2']=='XX':
		igra['8']='O'
	pass
	
	
		
xod='X'
for i in range(9):
	printxo(xo)
	print('Ваш ход:')
	i=input()
	xo[i]=xod
	comp(xo)
	#if xo[i]=='X':
		#xod='O'
	#else:
		#xod='X'

	
	
	



