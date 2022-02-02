class Robot:
    __population = 0

    def __init__(self, name):
        self.__name = name
        print(f'Робот {self.__name} был создан')
        Robot.__population += 1
        self.__isTrue=True

    @classmethod
    def how_many(cls):
        print(f'{cls.__population}, вот сколько нас еще осталось')

    def destroy(self):
        if self.__isTrue==True:
            Robot.__population-=1
        self.__isTrue=False
        print(f'Робот {self.__name} был уничтожен')

    def say_hello(self):
        print(f'Робот {self.__name} приветствует тебя, особь человеческого рода')



r2 = Robot("R2-D2") # печатает "Робот R2-D2 был создан"
r2.say_hello() # печатает "Робот R2-D2 приветствует тебя, особь человеческого рода"
Robot.how_many() # печатает "1, вот сколько нас еще осталось"
r2.destroy() # печатает "Робот R2-D2 был уничтожен"