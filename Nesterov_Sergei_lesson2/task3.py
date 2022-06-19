# Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить, к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и dict.

list_one = ['зима', 'весна', 'лето', 'осень']
dict_one = {1: 'зима', 2: 'весна', 3: 'лето', 4: 'осень'}
month = int(input("Введите месяц в виде целого числа от 1 до 12: "))
if month == 1 or month == 12 or month == 2:
    print(list_one[0])
    print(dict_one.get(1))
elif month == 3 or month == 4 or month == 5:
    print(list_one[1])
    print(dict_one.get(2))
elif month == 6 or month == 7 or month == 8:
    print(list_one[2])
    print(dict_one.get(3))
elif month == 9 or month == 10 or 11 == month:
    print(list_one[3])
    print(dict_one.get(4))
else:
    print('Ошибка! Введите число от 1 до 12')
