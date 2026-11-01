import numpy as np
from time import perf_counter
# 1Создай массив чисел от 1 до 10 через arange. Выведи его shape, dtype, ndim и size.

n = np.arange(1, 11)
print(n)
print(n.shape)
print(n.dtype)
print(n.ndim)
print(n.size)
print()
# 2 Создай матрицу 3×4 из нулей, матрицу 3×4 из единиц и единичную матрицу 4×4. Сделай из arange(12) матрицу 3×4 через reshape.

print(np.zeros((3, 4)))
print(np.ones((3,4)))
print(np.eye(4,4))
print(np.arange(12).reshape(3,4))
print()

# 3 Дан a = [1, 2, 3, 4, 5] и b = [10, 20, 30, 40, 50] (как NumPy-массивы). Без циклов получи a * 2, a ** 2, a + 10 и a + b.
a = np.arange(1,6)
b = np.arange(10, 51, 10)
print(a * 2)
print(a ** 2)
print(a + 10)
print(a + b)
print()
# 4 Создай m = np.arange(1, 21).reshape(4, 5). Выведи вторую строку ([ 6 7 8 9 10]), третий столбец ([ 3 8 13 18]), элемент в строке 2, столбце 3 (14) и подматрицу из строк 1–2 и столбцов 0–2 ([[ 6 7 8] [11 12 13]]).
c = np.arange(1, 21).reshape(4, 5)
print(c[1])
print(c[:,2])
print(c[2][3])
print(c[1:3, 0:3])
print()


# 5 Для a = np.arange(1, 21) с помощью масок: выбери чётные числа; выбери числа больше 5 и меньше 15; замени все числа, кратные 3, на 0.
a = np.arange(1, 21)
middel = a[(a > 5) & (a < 15)]
b = a.copy()
b[b % 3 == 0] = 0
print(middel)
print(b)
print()

# 6 Для m = np.array([[3, 7, 1], [9, 2, 8], [4, 6, 5]]) найди сумму и среднее всех элементов, сумму по столбцам (ожидается [16 15 14]), сумму по строкам ([11 19 15]) и индекс максимума в каждой строке ([1 0 1]).
m = np.array([[3, 7, 1], [9, 2, 8], [4, 6, 5]])
print(m.sum())
print(m.mean())
print(m.sum( axis = 0))
print(m.sum(axis = 1))
print(m.argmax(axis=1))
print()


# 7Для той же матрицы m выполни стандартизацию по столбцам: вычти среднее каждого столбца и раздели на его стандартное отклонение (через broadcasting, без циклов). Проверь, что среднее каждого столбца теперь около 0, а std равно 1.
z = (m - m.mean(axis=0)) / m.std(axis=0)
print(z)
print(z.mean(axis=0))   # около 0 (могут быть крошечные числа вроде 1e-17)
print(z.std(axis=0)) 
print()
# 8Даны точки p = [1, 2, 3] и q = [4, 6, 3]. Найди расстояние между ними: sqrt от суммы квадратов разностей. Ожидается 5.0.
p = np.array([1, 2, 3])
q = np.array([4, 6, 3])
d = q - p
print(np.sqrt((d**2).sum()))
print()
# 9Для v = [1, 2, 3] и w = [4, 5, 6] найди скалярное произведение тремя способами: вручную (сумма произведений), через np.dot и через @. Ожидается 32.
v = np.array([1, 2, 3])
w = np.array([4, 5, 6])
re = v * w
re1 = v@w
print(re.sum())
print(np.dot(v,w))
print(re1)
print()
# 10Построй таблицу умножения 9×9 без циклов: умножь столбец arange(1, 10).reshape(9, 1) на строку arange(1, 10).
t = np.arange(1, 10).reshape(9, 1) 
l = np.arange(1, 10)
print(t*l)

# 11 Создай матрицу 5×5 из случайных целых чисел от 0 до 99 (default_rng(42)).
#  Найди максимальный элемент и его положение (строка и столбец). Подсказка: np.argmax и np.unravel_index.
rng = np.random.default_rng(42)

i = rng.integers(0,100, size = (5,5))
maxx = np.argmax(i)
polozh = np.unravel_index(maxx,i.shape)
print(i.max())
print(maxx)
print(polozh)
print()
# 12 Вычти из каждой строки матрицы из задачи 11 её среднее значение. Подсказка: mean(axis=1, keepdims=True).
print(i - i.mean(axis=1, keepdims=True))
print()
# 13 Для A = [[1, 2], [3, 4]] и B = [[5, 6], [7, 8]] посчитай A * B ([[ 5 12] [21 32]]),
#  A @ B ([[19 22] [43 50]]) и A.T. Своими словами запиши, чем отличаются первые два результата.
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
print(A * B)
print(A @ B)
print(A.T)
print('В первом случае умножение поэлементно а во втором матричное умножение')
print()

# 14 Сгенерируй 1000 чисел из нормального распределения (rng.normal(0, 1, 1000), seed 42).
#  Найди среднее (около 0), std (около 1) и долю чисел между −1 и 1 (около 0.68).
rng = np.random.default_rng(42)
x = rng.normal(0, 1, 1000)
print(x.mean())
print(x.std())
big = ((x > -1) & (x < 1))        
print(big.mean())

print()
# 15 Сравни скорость: посчитай сумму квадратов чисел от 0 до 999 999 циклом for и через NumPy. 
#Замерь время через time.perf_counter(). NumPy должен оказаться в десятки раз быстрее.
start = perf_counter()
n1 = np.arange(1000000)
r = n1 ** 2
end = perf_counter()
print(end - start)
total = 0
start1 = perf_counter()
for  k in range(1000000):
    total += k ** 2
end1 = perf_counter()
print(end1-start1)