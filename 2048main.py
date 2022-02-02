import random
from random import choice

mas=[
	[1,0,1,1],
	[0,1,1,1],
	[1,1,1,1],
	[1,1,1,0],
	]

def pretty_mas(mas):
	print('-'*10)
	for i in mas:
		print(*i)
	print('-'*10) 

def empty_slot(mas):
	empty=[]
	for i in range(4):
		for j in range(4):
			if mas[i][j]==0:
				num=numer(i,j)
				empty.append(num)
	print(empty)
	print(random.choice(empty))
	
						
		
def numer(i,j):
	return i*4+j+1
	
def numer_return(num):
	num-=1
	i,j=num//4,num%4
	return i,j
	
	
def random(mas,i,j):
	if random.random()>=0.75:
		mas[i][j]=2
	else:
		mas[i][j]=4
	return mas
	
empty_slot(mas)
