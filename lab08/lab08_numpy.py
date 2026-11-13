import numpy as np


hours = np.arange(0, 22, 3)
line = np.linspace(0, 1, 5)
zeros = np.zeros(6, dtype=int)
unknown_table = np.full((2, 3), -1)
identity = np.eye(3)

print("hours:", hours)
print("hours shape:", hours.shape)
print("hours ndim:", hours.ndim)
print("hours size:", hours.size)
print("hours dtype:", hours.dtype)


print("Третий элемент:", hours[2])
print("Последний элемент:", hours[-1])
print("Элементы с индексами 2-5:", hours[2:6])
print("Каждый второй элемент:", hours[::2])
print("В обратном порядке:", hours[::-1])


temperatures = np.array([
    [12, 14, 13, 15],
    [11, 13, 16, 17],
    [10, 12, 15, 18],
])

print("Форма:", temperatures.shape)
print("Число измерений:", temperatures.ndim)
print("Число элементов:", temperatures.size)
print("Значение из 2-й строки и 3-го столбца:", temperatures[1, 2])
print("Первая строка:", temperatures[0])
print("Последний столбец:", temperatures[:, -1])
print("Первые две строки без первого столбца:\n", temperatures[:2, 1:])

central_block = temperatures[0:2, 1:3]
print("Центральный фрагмент 2x2:\n", central_block)
print("Его форма:", central_block.shape)


matrix = np.arange(1, 26).reshape(5, 5)

print("Первые три строки:\n", matrix[:3])
print("shape:", matrix[:3].shape)

print("Последние две строки:\n", matrix[3:])
print("shape:", matrix[3:].shape)

print("Первые два столбца:\n", matrix[:, :2])
print("shape:", matrix[:, :2].shape)

print("Фрагмент из строк 1-3 и столбцов 2-4:\n", matrix[1:4, 2:5])
print("shape:", matrix[1:4, 2:5].shape)

print("Угловой блок 2x2 в правом нижнем углу:\n", matrix[-2:, -2:])
print("shape:", matrix[-2:, -2:].shape)


vector = np.array([10, 20, 30, 40, 50])
vector[1:4] = 0

small_matrix = np.arange(1, 10).reshape(3, 3)
small_matrix[0, :] = -1
small_matrix[1:, 1:] = 9

changed_hours = hours.copy()
changed_hours[2:5] = 99
changed_hours[::2] = -1

print("changed_hours:", changed_hours)
print("Исходный hours:", hours)



changed_matrix = matrix.copy()
changed_matrix[1, :] = 0
changed_matrix[:, -1] = -1
changed_matrix[1:4, 1:4] = 100

print("Итоговая матрица:\n", changed_matrix)
print("Исходная матрица:\n", matrix)


numbers = np.arange(12)
table = numbers.reshape(3, 4)
transposed = table.T

print("Форма numbers:", numbers.shape)
print("Форма table:", table.shape)
print("Форма transposed:", transposed.shape)

