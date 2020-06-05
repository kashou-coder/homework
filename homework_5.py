"""1) Создать программно файл в текстовом формате, записать в него построчно данные,
вводимые пользователем. Об окончании ввода данных свидетельствует пустая строка."""

list_new = input("Введите текст: ").split()
print(list_new)
with open("create_file.txt", "x") as file:
    for i in list_new:
        file.write(i + "\n")
list_new = open("create_file.txt", "r")
content = list_new.read()
print(content)
list_new.close()

"""2) Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить
подсчет количества строк, количества слов в каждой строке."""

count = 0
with open("t_2_les_5.txt", "r") as file:
    for sting in file:
        count += 1
    print(count)

lst = open("t_2_les_5.txt", "r")
content = lst.read()
content = content.split()
content_1 = len(content)
print(content_1)
lst.close()

"""3) Создать текстовый файл (не программно), построчно записать фамилии сотрудников и
величину их окладов (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее
20 тыс., вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода
сотрудников.
Пример файла:
Иванов 23543.12
Петров 13749.32  """

list_workers = open("t_3_les_5.txt", "r")
content = list_workers.readlines()
for line in content:
    print(line.strip())

list_workers.close()
#
list_workers = open("t_3_les_5.txt", "r")
onstring = list_workers.read().split("\n")[:-1]
print(onstring)
dict = dict()
for item in onstring:
    key = item.split(" ")[0]
    value = item.split(" ")[1]
    dict[key] = value
value = float(value)
print(dict)
dict = list(dict.items())
print(dict)
dict.sort(key=lambda i: i[1])
print(dict)
for i in dict:
    print(i[0], ':', i[1])
list_workers.close()

"""4) Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно
данные. При этом английские числительные должны заменяться на русские. Новый блок строк
должен записываться в новый текстовый файл. """

num = open("t_4_les_5.txt", "r")
num_1 = num.readlines()
for line in num_1:
    print(line.strip())
num.close()

num_1 = open("t_4_les_5_1.txt", "w")
list_new = ["Один - 1\n", "Два - 1\n", "Три - 3\n", "Четыре - 4\n", "Пять - 5\n"]
num_1.writelines(list_new)
num_1.close()
num_1 = open("t_4_les_5_1.txt", "r")
content = num_1.read()
print(content)
num_1.close()

"""5) Создать (программно) текстовый файл, записать в него программно набор чисел,
разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить
ее на экран."""

num = open("t_5_less_5.txt", "w")
list_1 = num.write("1 2 3 4 5")
num.close()
num = open("t_5_less_5.txt", "r")
content = num.read()
print(content)
content_1 = list(map(int, content.split()))
suma = 0
for i in content_1:
    suma += i
print(suma)
num.close()

"""6) Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный
предмет и наличие лекционных, практических и лабораторных занятий по этому предмету и их
количество. Важно, чтобы для каждого предмета не обязательно были все типы занятий.
Сформировать словарь, содержащий название предмета и общее количество занятий по
нему. Вывести словарь на экран.
Примеры строк файла: Информатика: 100(л) 50(пр) 20(лаб).
Физика: 30(л) — 10(лаб)
Физкультура: — 30(пр) —
Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}  """

lst = open("t_6_les_5.txt", "r")
content = lst.read().split("\n")[:-1]
print(content)
dict = dict()
for item in content:
    key = item.split(" ")[0]
    value = item.split(" ")[1:4]
    dict[key] = value
print(dict)
lst.close()


"""7) Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая
строка должна содержать данные о фирме: название, форма собственности, выручка,
издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также
среднюю прибыль. Если фирма получила убытки, в расчет средней прибыли ее не включать .
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а
также словарь со средней прибылью. Если фирма получила убытки, также добавить ее в
словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{ "firm_1" : 5000 , "firm_2" : 3000 , "firm_3" : 1000 }, { "average_profit" : 2000 }]  """

firm = open("t_7_les_5.txt", "r")
lst = firm.readline().split()
print(lst)
lst_1 = tuple(lst)
lst_2 = dict(zip(lst_1[::2], lst_1[1::2]))
print(lst_2)
firm.close()