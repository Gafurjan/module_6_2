class Vehicle:
    __COLOR_VARIANTS = ['white', 'black', 'green', 'red', 'yellow', 'silver']

    def __init__(self, owner : str, model : str, color: str, engine_power: int):
        self.owner = owner
        self.__model = model
        self.__engine_power = engine_power
        self.__color = color

    def about(self):
        return self.__COLOR_VARIANTS


class Sedan(Vehicle):
    def get_model(self):
        return f'Модель: {self._Vehicle__model}'

    def get_horsepower(self):
        return f'Мощность двигателя: {self._Vehicle__engine_power}'

    def get_color(self):
        return f'Цвет: {self._Vehicle__color}'

    def print_info(self):
        print(self.get_model())
        print(self.get_horsepower())
        print(self.get_color())
        print(f'Владелец: {self.owner}')


    def set_color(self, new_color: str):
        if new_color in self._Vehicle__COLOR_VARIANTS:
            self._Vehicle__color = new_color
        else:
            print(f'Нельзя сменить цвет на {new_color}')



# sedan = Sedan('gafur', 'Camry', 70, 'white')
#
# print(dir(sedan))
#
# sedan.print_info()
# sedan.set_color('red')
# sedan.print_info()



# Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()