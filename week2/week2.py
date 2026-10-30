import json 

#Дан список [3, 8, 1, 14, 7, 20]. Создай список только из чисел больше 5, каждое умножь на 2. Ожидается [16, 28, 14, 40].
lst = [3, 8, 1, 14, 7, 20]
lst_res = [i*2 for i in lst if i > 5]

print(lst_res)

#Из строки "Python is fun" получи список длин слов через включение. Ожидается [6, 2, 3].

s = "Python is fun"
lst_res1 = [len(i) for i in s.split()]

print(lst_res1)

#Создай словарь {число: квадрат} для чисел от 1 до 6 через включение

dic = {k:k**2 for k in range(1,7)}
print(dic)


#Дан список строк [" apple ", "Banana", " cherry"]. 
# Получи список без пробелов по краям и с маленькой буквы: ['apple', 'banana', 'cherry'].
lst3 = [" apple ", "Banana", " cherry"]
lst_res3 = [u.lower().strip() for u in lst3]
print(lst_res3)

#Дан список ["a", "b", "a", "c", "b", "a"].
#  Посчитай, сколько раз встречается каждый элемент, и выведи самый частый. Ожидается a
lst4 = ["a", "b", "a", "c", "b", "a"]
count = 0

for o in lst4:
    if  lst4.count(o) > count:
        count = lst4.count(o)
        max_res = o
print (max_res)


#Даны два списка: names = ["Анна", "Иван"], scores = [90, 75]. Собери словарь {"Анна": 90, "Иван": 75}

names = ["Анна", "Иван"]
scores = [90, 75]

res_dict = dict(zip(names, scores))
print(res_dict)


#Даны два списка [1, 2, 3, 4] и [3, 4, 5, 6].
#  Найди числа, которые есть в обоих, числа, которые есть только в первом, и все уникальные числа вместе.

a = [1, 2, 3, 4]
b = [3, 4, 5, 6]

print (set(a) & set(b))
print(set(a) - set(b))
print(set(a) | set(b))

#Проверь, есть ли в списке повторяющиеся элементы, используя множество. Для [1, 2, 3, 2] ответ True, для [1, 2, 3] ответ False

c = [1, 2, 3,2]
print(len(set(c)) != len(c))


#Напиши программу, которая просит ввести два числа и выводит результат деления.
#Обработай ввод не числа и деление на ноль, чтобы программа не падала.
try:
    a, b = map(int,input().split())
    print(a/b)
except ValueError: 
    print("Введите число")
except ZeroDivisionError:
    print("На ноль делить нельзя")
else:
    print("Ошибок не было")

#Напиши функцию safe_int(text), которая возвращает число из строки, а если не получилось, возвращает None.
#  Проверь на "42", "abc", "".

def safe_int(text):
    try:
        return int(text)
    except ValueError:
        return None
    
print(safe_int('42'))

while True:
    try:
        n = int(input("Введите число: "))
        break
    except ValueError:
        print("Это не число, попробуйте ещё раз")
print("Вы ввели", n)


#Запиши в файл numbers.txt числа от 1 до 10, каждое на новой строке. Потом прочитай файл и выведи сумму.
with open('numbers.txt','w',encoding='utf-8') as f:
         for i in range(1,11):
            f.write(f"{i}\n")
with open('numbers.txt', 'r', encoding='utf-8') as t:
    total = 0
    for i in t:
        total += int(i.strip())
print(total)
#Сохрани словарь {"name": "Анна", "age": 20, "skills": ["Python", "SQL"]} в profile.json с русскими буквами без экранирования.
#  Загрузи его обратно и выведи навыки.
dictit = {"name": "Анна", "age": 20, "skills": ["Python", "SQL"]}
with open('profile.json', 'w',encoding='utf-8') as k:
    json.dump(dictit, k, ensure_ascii = False,indent=2)
with open('profile.json', 'r',encoding='utf-8') as l:
    res = json.load(l)
print(res['skills'])




#Напиши функцию load_data(path): если файла нет, она возвращает пустой список, а не падает. Подсказка: FileNotFoundError.
def load_data(path):
    try:
        with open(path, 'r',encoding='utf-8') as i:
            return json.load(i)
    except FileNotFoundError:
        return []
    
print(load_data("profile.json"))     # должен вернуться словарь Анны
print(load_data("net_takogo.json"))  # должен вернуться []
#Создай класс Rectangle с атрибутами width и height и методами area() и perimeter(). Проверь на прямоугольнике 3×5: площадь 15, периметр 16.
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height
    def perimetr(self):
        return ((self.width + self.height)*2)

rec1 = Rectangle(3,5)
print(rec1.area())
print(rec1.perimetr())




#Создай класс BankAccount с балансом и методами deposit(amount) и withdraw(amount).
# Если на счёте не хватает денег, выбрасывай ValueError.
class BankAccount:
    
    def __init__(self):
        self.balance = 0

    def deposit(self,f):
        self.balance += f
        
    def withdraw(self,n):
        if n > self.balance:
            raise ValueError("Нельзя вычесть больше, чем есть")
        self.balance -= n
        


bank1 = BankAccount()
bank1.deposit(1000)
bank1.withdraw(900)
print(bank1.balance)
#Создай класс Expense (название, сумма, категория) и метод info(). Сделай список из трёх объектов и посчитай общую сумму по категории.
class Expense:
    def __init__(self,name, summ, category):
        self.name = name
        self.summ = summ
        self.category = category
    def info(self):
        return f"{self.name} : {self.summ} , category : {self.category}"

expenses = [
    Expense('Ашан', 250, 'еда'),
    Expense('Автобус',73,'транспорт'),
    Expense('Виноград', 100, 'еда')
]
for i in expenses:
    print(i.info())

def total_by_category(expenses, category):
    total = 0
    for k in expenses:
        if k.category  == category:
            total += k.summ
    return total

print(total_by_category(expenses, 'еда'))