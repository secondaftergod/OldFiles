
class Money:
	def __init__(self,dollars,cents):
		self.total_cents=dollars*100+cents
	def __str__(self):
		return f'Ваше состояние составляет {self.dollars} долларов {self.cents} центов'
	@property
	def dollars(self):
		return self.total_cents//100
	@dollars.setter
	def dollars(self,new_d):
		if isinstance(new_d,int) and new_d>=0:
			self.total_cents = (self.total_cents - self.dollars*100) + new_d * 100
		else:
			print('Error dollars')
	@property
	def cents(self):
		return self.total_cents%100
	@cents.setter
	def cents(self,new_c):
		if isinstance(new_c,int) and new_c>=0 and new_c<100:
			self.total_cents=(self.total_cents-self.total_cents%100)+new_c
		else:
			print('Error cents')

Bill = Money(101, 99)
print(Bill)  # Ваше состояние составляет 101 долларов 99 центов
print(Bill.dollars, Bill.cents)  # 101 99
Bill.dollars = 666
print(Bill)  # Ваше состояние составляет 666 долларов 99 центов
Bill.cents = 12
print(Bill)  # Ваше состояние составляет 666 долларов 12 центов


class Square:
    def __init__(self,s):
        self.__side=s
        self.__area=None
    @property
    def side(self):
        return self.__side

    @side.setter
    def side(self, val):
        self.__side = val
        self.__area=None
    @property
    def area(self):
        if self.__area==None:
            self.__area=self.side**2
        return self.__area

a=Square(5)
