import numpy as np

def det(matrix):
    #Используем функцию linalg.det() для вычисления определителя матрицы
    determinant = np.linalg.det(matrix)
    return determinant

def solve(matrix_A, matrix_b):
    #Используем функцию linalg.solve() для решения системы уравнений
    solution = np.linalg.solve(matrix_A, matrix_b)
    return solution

#Пример использования функций
matrix_A = np.array([[1, 2], [3, 4]])
matrix_b = np.array([5, 6])

#Вычисление определителя матрицы
determinant = det(matrix_A)
print("Определитель матрицы A:", determinant)

#Решение системы уравнений
solution = solve(matrix_A, matrix_b)
print("Решение системы уравнений Ax = b:", solution)
