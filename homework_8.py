"""1) Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде
строки формата «день-месяц-год». В рамках класса реализовать два метода. Первый, с
декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к
типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа,
месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на
реальных данных."""

import datetime

class Date_1:

    @classmethod
    def mymethod_date(cls, yyyy, mm, dd):
        date_o = datetime.datetime(yyyy, mm, dd)
        print(date_o)
        date_o = date_o.timetuple()
        print(date_o)
        for i in date_o:
            print(i)

    @staticmethod
    def valid(yyyy, mm, dd):
        try:
            date_o = datetime.datetime(yyyy, mm, dd)
            print(date_o)

        except ValueError:
            print("Введена некорректная дата! Следовало ввести ГГГГ-ММ-ДД")

Date_1.mymethod_date(2019, 12, 31)
Date_1.valid(2019, 12, 31)

"""2) Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля в
качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с
ошибкой. """

import traceback

def zero():
    try:
        a = int(input("Введите любое первое число: "))
        b = int(input("Введите любое второе число: "))
        c = a / b
        print(c)
    except Exception as e:
        print('Ошибка (на ноль делить нельзя!):\n', traceback.format_exc())

a = zero()


"""3) Создайте собственный класс-исключение, который должен проверять содержимое списка на
наличие только чисел. Проверить работу исключения на реальном примере. Необходимо
запрашивать у пользователя данные и заполнять список только числами. Класс-исключение
должен контролировать типы данных элементов списка.
Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно, пока
пользователь сам не остановит работу скрипта, введя, например, команду “stop”. При этом
скрипт завершается, сформированный список с числами выводится на экран.
Подсказка: для данного задания примем, что пользователь может вводить только числа и
строки. При вводе пользователем очередного элемента необходимо реализовать проверку
типа элемента и вносить его в список, только если введено число. Класс-исключение должен
не позволить пользователю ввести текст (не число) и отобразить соответствующее
сообщение. При этом работа скрипта не должна завершаться."""

import traceback

def exceptionlist():
    try:
        while True:
            list_new = input("Введите числа через пробел (stop): ").split()
            for i in list_new:
                i = int(i)
                print(i)
            if list_new == 'stop':
                break
    except Exception as j:
        print("Ошибка: Вы ввели некорректный тип данных!\n", traceback.format_exc())

a = exceptionlist()

"""4) Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А
также класс «Оргтехника», который будет базовым для классов-наследников. Эти классы —
конкретные типы оргтехники (принтер, сканер, ксерокс). В базовом классе определить
параметры, общие для приведенных типов. В классах-наследниках реализовать параметры,
уникальные для каждого типа оргтехники. """

class Warehouse:
   pass

class OfficeEquipment:
    def __init__(self, type, brand, model):
        self.type = type
        self.brand = brand
        self.model = model

    def __str__(self):
        return f'Тип бренд и модель: {self.type} {self.brand} {self.model}'

class Printer (OfficeEquipment):
    def Output(self):
        print("Печать документа!")

class Scanner(OfficeEquipment):
    def scan(self):
        print("Сканирование документа на PC в формате PDF!")

class Copier(OfficeEquipment):
    def copiers(self):
        print("Копирование документа формата A4!")

a = OfficeEquipment("Принтер","ASUS", "a320")
print(a)
b = Printer("Принтер","ASUS", "a320")
b.Output()
c = Scanner("Сканер","HP", "b380")
print(c)
c.scan()
e = Copier("Ксерокс", "XEROX", "ewds43443")
print(e)
e.copiers()

"""5) Продолжить работу над первым заданием. Разработать методы, отвечающие за приём
оргтехники на склад и передачу в определенное подразделение компании. Для хранения
данных о наименовании и количестве единиц оргтехники, а также других данных, можно
использовать любую подходящую структуру, например словарь."""

class Warehouse:
   pass

class OfficeEquipment:
    def __init__(self, type, brand, model):
        self.type = type
        self.brand = brand
        self.model = model

    def dictionary(self):
        a = dict.fromkeys(["Тип техники"], self.type)
        b = dict.fromkeys(["Brand"], self.brand)
        c = dict.fromkeys(["Model"], self.model)
        print(f"{a} \n {b} \n {c}")

class Printer (OfficeEquipment):
    def Output(self):
        print("Печать документа!")

class Scanner(OfficeEquipment):
    def scan(self):
        print("Сканирование документа на PC в формате PDF!")

class Copier(OfficeEquipment):
    def copiers(self):
        print("Копирование документа формата A4!")

b = Scanner("Принтер","ASUS", "a320")
b.dictionary()

c = Scanner("Сканер","HP", "b380")
c.dictionary()




"""6) Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых
пользователем данных. Например, для указания количества принтеров, отправленных на
склад, нельзя использовать строковый тип данных.
 Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники»
максимум возможностей, изученных на уроках по ООП."""


class Warehouse:
    pass

class OfficeEquipment:
    def __init__(self, type, brand, model, kol):
        self.type = type
        self.brand = brand
        self.model = model
        self.kol = int(kol)

    def dictionary(self):
        a = dict.fromkeys(["Тип техники"], self.type)
        b = dict.fromkeys(["Brand"], self.brand)
        c = dict.fromkeys(["Model"], self.model)
        print(f"{a} \n {b} \n {c}")


class Printer(OfficeEquipment):
    def Output(self):
        print("Печать документа!")


class Scanner(OfficeEquipment):
    def scan(self):
        print("Сканирование документа на PC в формате PDF!")


class Copier(OfficeEquipment):
    def copiers(self):
        print("Копирование документа формата A4!")


b = Scanner("Принтер", "ASUS", "a320", "dsd")
b.dictionary()


"""7) Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное
число», реализуйте перегрузку методов сложения и умножения комплексных чисел.
Проверьте работу проекта, создав экземпляры класса (комплексные числа) и выполнив
сложение и умножение созданных экземпляров. Проверьте корректность полученного
результата."""


class Complex:
    def __init__(self, x, y):
        self.x = x
        self.y = y


    def oper(self):
        z = complex(self.x, self.y)
        print(z)
        c = complex(self.x + self.y)
        print(c)
        s = complex(self.x - self.y)
        print(s)
        a = complex(self.x * self.y)
        print(a)
        b = complex(self.x / self.y)
        print(b)

a = Complex(2, 21)
a.oper()





