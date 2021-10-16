from math import sqrt

class Point:

    list_points = []

    def __init__(self, coordinate_x=0, coordinate_y=0):
        self.move_to(coordinate_x, coordinate_y)
        Point.list_points.append(self)

    def move_to(self, coordinate_x=0, coordinate_y=0):
        self.x = coordinate_x
        self.y = coordinate_y

    def go_home(self):
        self.move_to(0, 0)

    def print_point(self):
        print(f'Точка с координатами {self.x, self.y}')

    @staticmethod
    def calc_distance(another_point, self):
        if not isinstance(another_point, Point):
            raise ValueError('Аргумент не точка')
        return sqrt((self.x-another_point.x)**2 + (self.y-another_point.y)**2)