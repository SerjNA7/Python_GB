# Пользователь вводит строку из нескольких слов, разделённых пробелами.
# Вывести каждое слово с новой строки. Строки нужно пронумеровать.
# Если слово длинное, выводить только первые 10 букв в слове.

num_str = input("Напишите строку:")
my_word = []
num = 1
for a in range(num_str.count(" ") + 1):
    my_word: list[str] = num_str.split()
    if len(str(my_word)) > 10:
        print(f" {num} {my_word[a][0:10]}")
        num += 1
    else:
        print(f" {num} {my_word[a]}")
        num += 1
