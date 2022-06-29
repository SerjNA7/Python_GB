# Создать (программно) текстовый файл, записать в него программно набор чисел, разделённых пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить её на экран.

def num():
    try:
        with open("task5_test.txt", 'w+') as file_obj:
            li = input("Напишите цифры: ")
            file_obj.writelines(li)
            my_numb = li.split()
            print(sum(map(int, my_numb)))
    except ValueError:
        print("Error!!!")
num()
