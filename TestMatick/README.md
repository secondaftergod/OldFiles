"""You have objects:circle,triangle,trapeze,square in class Generation.
You can change a color,sizes after 'generation.random'(for example: generation.circle.color='black', generation.square.side=5)
Circe info:
circle.radius # радіус
circle.s # площа
Triange info:
triangle.k1 #катет
triangle.k2 # катет
Automatic calculation 'gip'
triangle.gip # гіпотенуза
triangle.s # площа
Square info:
square.side #сторона квадрата
square.s
Trapeze info:
trapeze.side_left
trapeze.side_right
trapeze.side_up
trapeze.side_down
trapeze.h # висота трапеції
trapeze.s # площа
"""
"""You can work whithout random generation figures
Create object figure,for example:
circle=figures.Circle()
circle.radius=5 # встановелння радіуса
circle.color='yellow' # колір для фігури
circle.visual() 
print(cirlce.s)# виводить площу"""