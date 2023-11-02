#Создание класса STUDENT
class STUDENT:
    def __init__(self, full_name, group_number, grades):
        self.full_name = full_name
        self.group_number = group_number
        self.grades = grades

    def has_unsatisfactory_grade(self):
        #Проверяем, есть ли хотя бы одна неудовлетворительная отметка меньше 4
        for grade in self.grades:
            if grade < 4:
                return True
        return False

#Создание массива студентов
students = []
for i in range(10):
    print(f"Введите данные для студента {i + 1}:")
    full_name = input("Фамилия и инициалы: ")
    group_number = input("Номер группы: ")
    grades = []
    for j in range(5):
        grade = int(input(f"Оценка {j + 1}: "))
        grades.append(grade)

    #Создаем объект типа STUDENT и добавляем его в массив
    student = STUDENT(full_name, group_number, grades)
    students.append(student)

#Вывод студентов с неудовлетворительными оценками
found_students = False
for student in students:
    if student.has_unsatisfactory_grade():
        print(f"Студент: {student.full_name}, Группа: {student.group_number}")
        found_students = True

if not found_students:
    print("Нет студентов с неудовлетворительными оценками.")
