# Реализуйте базовый класс Car.
# у класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала,
# остановилась, повернула (куда);
# опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
# добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
# для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Вызовите методы и покажите результат.

class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f"{self.name} Поехал"

    def stop(self):
        return f"{self.name} Тормозит!"

    def turn_right(self):
        return f"{self.name} Поворачиваем направо"

    def turn_left(self):
        return f"{self.name} Поворачиваем налево"

    def show_speed(self):
        return f"Скорость {self.name} {self.speed}"


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f"Текущая скорость {self.name} {self.speed}")

        if self.speed > 60:
            return f"Скорость {self.name} выше разрешенной"
        else:
            return f"Скорость {self.name} нормальная"

class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f"Текущая скорость {self.name} {self.speed}")

        if self.speed > 80:
            return f"Скорость {self.name} выше разрешенной"


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police(self):
        if self.is_police:
            return f"{self.name} из отдела полиции"
        else:
            return f"{self.name} не из отдела полиции"


Nissan = SportCar(60, "White", "Nissan", False)
Toyota = TownCar(60, "Black", "Toyota", False)
BMW = WorkCar(230, "Red", "BMW", True)
Skoda = PoliceCar(170, "Blue", "Skoda", True)
print(BMW.turn_left())
print(f"Когда {Toyota.turn_right()}, тогда {Nissan.stop()}")
print(f"{BMW.go()} с высокой скоростью {BMW.show_speed()}")
print(f"{BMW.name} {BMW.color}")
print(f"За {Nissan.name} Полиция? {Nissan.is_police}")
print(f"За {BMW.name}  Полиция? {BMW.is_police}")
print(Nissan.show_speed())
print(Toyota.show_speed())
print(Skoda.police())
print(Skoda.show_speed())