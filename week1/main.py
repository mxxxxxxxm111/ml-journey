#Выведи все числа от 1 до 100, которые делятся на 3 или на 5
for i in range(1,101):
    if i % 3 == 0 or i % 5 == 0:
        print(i)


#Напиши программу, которая печатает таблицу умножения от 1 до 9 в виде сетки
for i in range(1,10):
    for j in range(1,10):
        print(i * j, end = " ")
    print()

#Дан список чисел. Выведи только чётные, а затем создай новый список из квадратов всех чисел через списковое включение.
lst = list(map(int, input().split()))
print(*[n for n in lst if n % 2 == 0])

lst2 = [o ** 2 for o in lst]
print(*lst2)




#Разверни список без использования reverse() и срезов [::-1]


lst3 = [1,2,3,4,5,6]
reversed_lst = []
for u in range(len(lst3) -1, -1, -1):
    reversed_lst.append(lst3[u])
print(reversed_lst)

# Дана строка. Подсчитай, сколько раз встречается каждое слово, и выведи словарь.?
p = input().split()
dic = {}
for k in p:

    dic[k] = dic.get(k, 0) + 1
print(dic)

# Дан словарь {"Анна": 85, "Иван": 62, "Мария": 91}. Выведи тех, у кого оценка выше 80, отсортировав по убыванию оценки.

d = {"Анна": 85, "Иван": 62, "Мария": 91}

print([k for k in sorted(d, key=d.get, reverse=True) if d[k] > 80])

# Объедини два словаря. Если ключ есть в обоих, значения должны сложиться.
d1 = {"Анна": 85, "Иван": 62, "Мария": 91}
d2 = {"Анна": 15, "Петя": 62, "Мария": 91, "Васич": 14.1}
result = d1.copy()
for x in d2:
    result[x] = result.get(x,0) + d2[x]
print(result)

# Сделай из словаря {"a": 1, "b": 2} словарь с поменянными местами ключами и значениями.
d5 = {"a": 1, "b": 2}
re = {}
for k,v in d5.items():
    re[v] = k
print(re)
#Посчитай сумму цифр целого числа, введённого пользователем (например, для 4721 ответ 14).
resu = 0
for ch in input():
    resu  += int(ch)
print(resu)

# 5 Найди в списке максимум, минимум и среднее, не используя max, min и sum.
minimum = lst3[0]
maximum = lst3[0]
summa = 0
for i in lst3:
    if minimum > i:
        minimum = i
    if maximum < i:
        maximum = i
    summa += i
print(f"max = {maximum}, min = {minimum}, srednee = {summa / len(lst3)}")

#Напиши функцию is_prime(n), которая возвращает True, если число простое. Выведи все простые числа до 50.
def is_prime(n):
    if n < 2: return False
    for g in range(2, n):
        if n % g == 0:
            return False
    return True
for h in range(51):
    if is_prime(h):
        print(h)

    

#Напиши функцию average(*numbers), которая принимает любое количество чисел и возвращает среднее. Для пустого вызова верни None.

def average(*numbers):
    if len(numbers) == 0:
        return None
    summma = 0
    for l in numbers:
        summma += l
    return summma/ len(numbers)


#Напиши функцию word_stats(text), которая возвращает словарь с числом слов, самым длинным словом и средней длиной слова.

def word_stats(text):
    words = text.split()
    if not words:
        return {"words": 0, "longest": None, "avg_len": 0}
    return {
        "words": len(words),
        "longest": max(words, key=len),
        "avg_len": sum(len(w) for w in words) / len(words),
    }

        





    
#Напиши функцию fizzbuzz(n), которая возвращает список из n элементов. Вместо чисел, кратных 3, пишется "Fizz", кратных 5 "Buzz", кратных обоим "FizzBuzz".

def fizzbuzz(n):
    res_lst = []
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            res_lst.append('FizzBuzz')
        elif i % 3 == 0:
            res_lst.append('Fizz')
        elif i % 5 == 0:
            res_lst.append('Buzz')
        else:
            res_lst.append(i)
    return res_lst
