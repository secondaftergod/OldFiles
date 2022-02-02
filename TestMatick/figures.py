import random
import matplotlib.pyplot as plt
import matplotlib.patches as patches


class Circle:
    def __init__(self, radius=0, color=None):
        self._radius = radius
        self.s = 0
        self._color = color

    @property
    def radius(self):
        return self._radius

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, new_color):
        self._color = new_color

    @radius.setter
    def radius(self, new_radius):
        Triangle.check_value(new_radius)
        self._radius = new_radius
        self.s = 3.14 * new_radius * new_radius

    @staticmethod
    def check_value(value):
        if value <= 0 and value != int():
            raise Exception

    def visual(self):
        circle1 = plt.Circle((0, 0), self._radius, color=f'{self._color}', fill=True)
        ax = plt.gca()
        ax.add_patch(circle1)
        plt.axis('scaled')
        plt.show()

    def __str__(self):
        return f'Коло площею {self.s:.3f},радіусом:{self.radius:.3f},кольором {self._color}'


class Triangle:
    def __init__(self, k1=0, k2=0, color=None):
        self._k1 = k1
        self.s = 0
        self._color = color
        self._k2 = k2
        self.gip = 0

    @property
    def k1(self):
        return self._k1

    @property
    def k2(self):
        return self._k2

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, new_color):
        self._color = new_color

    @k1.setter
    def k1(self, new_k1):
        Triangle.check_value(new_k1)
        self._k1 = new_k1
        if self._k1 != 0 and self._k2 != 0:
            self.s = 1 / 2 * self._k1 * self._k2
            self.gip = (self._k1 ** 2 + self._k2 ** 2) ** 0.5

    @k2.setter
    def k2(self, new_k2):
        Triangle.check_value(new_k2)
        self._k2 = new_k2
        if self._k1 != 0 and self._k2 != 0:
            self.s = 1 / 2 * self._k1 * self._k2
            self.gip = (self._k1 ** 2 + self._k2 ** 2) ** 0.5

    @staticmethod
    def check_value(value):
        if value <= 0 and value != int():
            raise Exception

    def visual(self):
        if self._k1 != 0 and self._k2 != 0:
            fig = plt.figure()
            path = [
                [0, 0],
                [0, self._k1],
                [self._k2, 0],
            ]
            ax = fig.gca()
            plt.axis([0, self._k1 + 4, 0, self._k2 + 4])
            ax.add_patch(patches.Polygon(path, facecolor=f'{self._color}'))
            plt.show()
        else:
            print('Не вистачає даних для побудови фігури')

    def __str__(self):
        return f'Трикутник площею {self.s:.3f},гіпотенуза:{self.gip:.3f},кольором {self._color}'


class Square:
    def __init__(self, side=0, color=None):
        self._side = side
        self._color = color
        self.s = 0

    @property
    def side(self):
        return self._side

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, new_color):
        self._color = new_color

    @side.setter
    def side(self, new_side):
        Square.check_value(new_side)
        self._side = new_side
        self.s = self._side ** 2

    @staticmethod
    def check_value(value):
        if value <= 0 and value != int():
            raise Exception

    def visual(self):
        plt.axes()
        rectangle = plt.Rectangle((0, 0), self._side, self._side, color=f'{self._color}', fill=True)
        plt.gca().add_patch(rectangle)
        plt.axis('scaled')
        plt.show()

    def __str__(self):
        return f'Прямокутник площею {self.s},стороною:{self.side},кольором {self._color}'


class Trapeze:
    def __init__(self, side_left=0, side_right=0, side_up=0, side_down=0, color=None):
        self._side_left = side_left
        self._side_right = side_right
        self._side_up = side_up
        self._side_down = side_down
        self._color = color
        self.s = 0
        self.h = 0

    @property
    def side_left(self):
        return self._side_left

    @property
    def side_right(self):
        return self._side_right

    @property
    def side_up(self):
        return self._side_up

    @property
    def side_down(self):
        return self._side_down

    @property
    def color(self):
        return self._color

    @side_left.setter
    def side_left(self, new_side_left):
        Square.check_value(new_side_left)
        self._side_left = new_side_left
        if self._side_left != 0 and self._side_right != 0 and self._side_up != 0 and self._side_down != 0:
            self.h = ((self._side_left ** 2) - (
                    ((((self._side_down - self._side_up) ** 2) + self._side_left ** 2 - self._side_right ** 2)) / (
                    2 * (self._side_down - self._side_up))) ** 2) ** 0.5
            self.s = ((self._side_up + self._side_down) / 2) * self.h

    @side_right.setter
    def side_right(self, new_side_right):
        Square.check_value(new_side_right)
        self._side_right = new_side_right
        if self._side_left != 0 and self._side_right != 0 and self._side_up != 0 and self._side_down != 0:
            self.h = ((self._side_left ** 2) - (
                    ((((self._side_down - self._side_up) ** 2) + self._side_left ** 2 - self._side_right ** 2)) / (
                    2 * (self._side_down - self._side_up))) ** 2) ** 0.5
            self.s = ((self._side_up + self._side_down) / 2) * self.h

    @side_up.setter
    def side_up(self, new_side_up):
        Square.check_value(new_side_up)
        self._side_up = new_side_up
        if self._side_left != 0 and self._side_right != 0 and self._side_up != 0 and self._side_down != 0:
            self.h = ((self._side_left ** 2) - (
                    ((((self._side_down - self._side_up) ** 2) + self._side_left ** 2 - self._side_right ** 2)) / (
                    2 * (self._side_down - self._side_up))) ** 2) ** 0.5
            self.s = ((self._side_up + self._side_down) / 2) * self.h

    @side_down.setter
    def side_down(self, new_side_down):
        Square.check_value(new_side_down)
        self._side_down = new_side_down
        if self._side_left != 0 and self._side_right != 0 and self._side_up != 0 and self._side_down != 0:
            self.h = ((self._side_left ** 2) - (
                    ((((self._side_down - self._side_up) ** 2) + self._side_left ** 2 - self._side_right ** 2)) / (
                    2 * (self._side_down - self._side_up))) ** 2) ** 0.5
            self.s = ((self._side_up + self._side_down) / 2) * self.h

    @color.setter
    def color(self, new_color):
        self._color = new_color

    @staticmethod
    def check_value(value):
        if value <= 0 and value != int():
            raise Exception

    def visual(self):
        fig = plt.figure()
        path = [
            [0, 0],
            [self._side_left / 4, self._side_left],
            [self._side_up, self._side_left],
            [self._side_down, 0],
        ]
        ax = fig.gca()
        plt.axis([0, self._side_down + 4, 0, self._side_down + 4])
        ax.add_patch(patches.Polygon(path, facecolor=f'{self._color}'))
        plt.show()

    def __str__(self):
        return f'Трапеція площею {self.s:.3f},висотою:{self.h:.3f},кольором {self._color}'


class Generation:
    circle = Circle()
    triangle = Triangle()
    square = Square()
    trapeze = Trapeze()
    color = ['black', 'blue', 'white', 'green', 'red', 'yellow']
    mass = list()

    def random(self, min, max):
        self.Circle.radius = random.randint(min, max)
        self.circle.color = random.choice(self.color)
        self.triangle.k1 = random.randint(min, max)
        self.triangle.k2 = random.randint(min, max)
        self.triangle.color = random.choice(self.color)
        self.square.side = random.randint(min, max)
        self.square.color = random.choice(self.color)
        self.trapeze.side_up = random.randint(min, max)
        self.trapeze.side_down = self.trapeze.side_up + random.randint(1, 3)
        self.trapeze.side_left = random.randint(min, max)
        self.trapeze.side_right = random.randint(min, max)
        self.trapeze.color = random.choice(self.color)
        self.mass = [self.triangle, self.circle, self.square, self.trapeze]
        random.shuffle(self.mass)
