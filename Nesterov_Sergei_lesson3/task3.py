# Реализовать функцию my_func(), которая принимает три позиционных аргумента и возвращает сумму
# наибольших двух аргументов.


def my_func(num1, num2, num3):
    if num1 > num3 and num2 > num3:
        return num1 + num2
    elif num1 > num2 and num1 <= num3:
        return num1 + num3
    else:
        return num2 + num3


print(
    f"Вывод: - {my_func(int(input('Напишите число: ')), int(input('Еще одно: ')), int(input('И еще одно: ')))}")


