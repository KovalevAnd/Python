# Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод init()),
# который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц вы найдете в методичке.
# Следующий шаг — реализовать перегрузку метода str() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода add() для реализации операции сложения двух объектов класса Matrix (двух матриц).
# Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы
# складываем с первым элементом первой строки второй матрицы и т.д.


class Matrix:
    def __init__(self, matrix):
        self.a = '\n'.join(['\t'.join([str(j) for j in i]) for i in matrix])
        b = []
        for i in matrix:
            b.append([j for j in i])
        self.matrix = b

    def __str__(self):
        self.d = str(self.a)
        return self.d

    def __add__(self, other):
        result = []
        numb = []
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                summa = self.matrix[i][j] + other.matrix[i][j]
                numb.append(summa)
                if len(numb) == len(self.matrix):
                    result.append(numb)
                    numb = []
        return Matrix(result)


a = [[2, 1], [2, 1]]
b = [[2, 2], [2, 2]]
m_1 = Matrix(a)
m_2 = Matrix(b)
print(m_1)
print(m_2)
print(m_1 + m_2)