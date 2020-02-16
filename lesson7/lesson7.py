# class Task1A:
#     pass


# class Task1B:
#     x = 1


# class Task1C(Task1B):


# class Task1D:
#     pass


# class Task1E(Task1D):
#     pass


# print(Task1C.x)
# # Описать такую систему наследований классов Task1A, Task1B, Task1C, Task1D, Task1E без повторений переменных, чтобы:
# # Переменная x со значением 1 доступна (но прописана только у одного) у классов Task1B и Task1C.
# # Переменная x = 2 перегружена в классе Task1A (она была бы = 1, если бы не написали x = 2).
# # В Task1D прописана переменная x = 3.
# # Task1C наследуется от Task1D (не факт, что только от него)
# # Task1A не наследуется от Task1C.
# # В Task1E не прописан x, но доступен со значением 3. Наследуется только от одного родителя.

# class Student:
#     UNIVERSITY = 'BSUIR'

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def __str__(self):
#         return f'{self.name} ({self.age})'


# class AliveStudent(Student):
#     def __init__(self, name, age, marks):
#         super().__init__(name, age)
#         self.marks = marks


# class ExpelledStudent(Student):
#     def __init__(self, name, age):
#         super().__init__(name, age)


# student_1 = AliveStudent('Alex', 20, [7, 10, 8])
# student_2 = ExpelledStudent('John', 22)
# print(student_1)
# print(student_2)


# 2


class Department:

    def __init__(self, name, budget, employees={}):
        self.name = name
        self.employees = employees
        self.budget = budget

    def __str__(self):
        return f'{self.name} ({self.budget}-{self.employees})'

    def __repr__(self):
        return str(self)

    def get_average_selary(self):
        lst = []
        for value in self.employees.values():
            lst.append(value)
            return round((sum(lst) / len(lst)), 2)


bsu = Department("bsu", 3000, {'vlad': 1000, 'nik': 3000})
print(bsu)
print(bsu.get_average_salary())
