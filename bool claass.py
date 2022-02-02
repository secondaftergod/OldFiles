class City:
    def __init__(self,name):
        self.name=name.title()
    def __str__(self):
        return self.name
    def __bool__(self):
        return self.name[-1] not in 'aeiou'
"""p1 = City('new york')
print(p1)  # печатает "New York"
print(bool(p1))"""

class Quadrilateral:
    def __init__(self,width,height=None):
        self.width=width
        self.height=height or width

    def __str__(self):
        if self.height==self.width:
            return f'Куб размером {self.width}x{self.height}'
        else:
            return f'Прямоугольник размером {self.width}x{self.height}'
    def __bool__(self):
        return self.height==self.width

q1 = Quadrilateral(10)
print(q1)  # печатает "Куб размером 10х10"
print(bool(q1))  # печатает "True"
q2 = Quadrilateral(3, 5)
print(q2)  # печатает "Прямоугольник размером 3х5"
print(q2 == True)  # печатает "False"


