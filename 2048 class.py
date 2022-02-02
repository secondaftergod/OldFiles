import random

class Board:
	mas=[
	[0,0,0,0],
	[0,2,0,0],
	[4,0,0,0],
	[4,0,2,0],
	]
	def open(self):
		for i in self.mas:
			print(*i)
	
	def empty(self):
		for i in range(4):
			for j in range(4):
				if self.mas[i][j]==0:
					return i,j
	
	def add(self):
		i,j=board.empty()	
		if random.random()>=0.65:
			self.mas[i][j]=4
		else:
			self.mas[i][j]=2
		board.open()
		
	def move_left(self):
		a=input()
		if a=='l':
			for row in self.mas:
				while 0 in row:
					row.remove(0)
				while len(row)!=4:
					row.append(0)
				row=self.mas
			for i in range(4):
				for j in range(4):
					self.mas[i][j]==self.mas
					
					
					
				
		
		
		
board=Board()
board.add()
board.move_left()

	
	

