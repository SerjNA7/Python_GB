# Выполнить функцию, которая принимает несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы. Осуществить вывод данных о пользователе одной строкой.


def func(name, surname, year, city, email, telephone):
    return " ".join([name, surname, year, city, email, telephone])


print(func(name="David", surname="Beckham", year="1975", city="London",
           email="GB_2022@mail.ru", telephone="8-903-111-11-11"))
