# Создать текстовый файл (не программно), сохранить в нём несколько строк,
# выполнить подсчёт строк и слов в каждой строке.


my_file = open("task2_test.txt")
content = my_file.read()
print(f'Текст: \n {content}')
my_file = open("task2_test.txt")
content = my_file.readlines()
print(f'Количество строк: {len(content)}')
my_file = open("task2_test.txt")
content = my_file.readlines()
for i in range(len(content)):
    print(f'Количество символов {i + 1} - строки {len(content[i])}')
my_file.close()
