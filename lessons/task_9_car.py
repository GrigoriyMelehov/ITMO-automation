class Car:

    def __init__(self, color = 'red', type = 'BMV', year = 1990):
        self.color = color
        self.type = type
        self.year = year

    def Car_start(self):
        print('"Автомобиль заведен"')

    def Car_stop(self):
        print('"Автомобиль заглушен"')

    def Car_year(self):
        self.year = 1991

    def Car_type(self):
        self.type = 'RENAULT'

    def Car_color(self):
        self.color = 'blue'

# Car_1 = Car()
#
# Car_1.Car_start()
# Car_1.Car_stop()
# print(Car_1.color, Car_1.type, Car_1.year)
# Car_1.Car_year()
# Car_1.Car_color()
# Car_1.Car_type()
# print(Car_1.color, Car_1.type, Car_1.year)

