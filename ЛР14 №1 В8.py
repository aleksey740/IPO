#Создание класса Больница
class Hospital:
    def __init__(self, name, director, city, address):
        #Инициализация атрибутов объекта
        self.name = name
        self.director = director
        self.city = city
        self.address = address

#Дочерний класс Отделение, наследуется от класса Больница
class Department(Hospital):
    def __init__(self, hospital_name, director, city, address, department_name, building, floor, head_doctor):
        #Вызов конструктора родительского класса с помощью super
        super().__init__(hospital_name, director, city, address)
        #Инициалллизация атрибутов отделения
        self.department_name = department_name
        self.building = building
        self.floor = floor
        self.head_doctor = head_doctor

#Дочерний класс Пациент наследуется от класса 0тделение
class Patient(Department):
    def __init__(self, hospital_name, director, city, address, department_name, building, floor, head_doctor):
        #Вызов конструктора родительского класса с помощью super()
        super().__init__(hospital_name, director, city, address, department_name, building, floor, head_doctor)
        # Ввод данных от пользователя для создания объекта пациента
        self.patient_name = input("Введите ФИО пациента: ")
        self.policy_number = input("Введите номер полиса: ")
        self.admission_date = input("Введите дату поступления (гггг-мм-дд): ")
        self.discharge_date = input("Введите дату выписки (гггг-мм-дд): ")
        self.diagnosis = input("Введите диагноз: ")
        self.operation_date = input("Введите дату проведения операции (гггг-мм-дд): ")
        self.operation_name = input("Введите название операции: ")
        self.treatment_cost = float(input("Введите стоимость лечения: "))

#Дочерний класс Доктор, наследуется от класса Отделение
class Doctor(Department):
    def __init__(self, hospital_name, director, city, address, department_name, building, floor, head_doctor):
        #Вызов конструктора родительского класса с помощью super
        super().__init__(hospital_name, director, city, address, department_name, building, floor, head_doctor)
         #Ввод данных
        self.doctor_name = input("Введите ФИО врача: ")
        self.position = input("Введите должность врача: ")
        self.academic_title = input("Введите научное звание врача: ")
        self.experience = int(input("Введите стаж работы врача (в годах): "))

#Пример использования
if __name__ == "__main__":
    #Ввод данных для обьекта больница
    hospital_name = input("Введите название больницы: ")
    director = input("Введите ФИО заведующего: ")
    city = input("Введите город: ")
    address = input("Введите адрес: ")

    #Ввод данных для обьекта отделение
    department_name = input("Введите название отделения: ")
    building = input("Введите корпус отделения: ")
    floor = int(input("Введите этаж отделения: "))
    head_doctor = input("Введите ФИО заведующего отделением: ")

    #Создание объектов
    hospital = Hospital(hospital_name, director, city, address)
    department = Department(hospital_name, director, city, address, department_name, building, floor, head_doctor)
    patient = Patient(hospital_name, director, city, address, department_name, building, floor, head_doctor)
    doctor = Doctor(hospital_name, director, city, address, department_name, building, floor, head_doctor)

    #Вывод информации об обьектах
    print(f"\nБольница: {hospital.name}")
    print(f"Отделение: {department.department_name}")
    print(f"Пациент: {patient.patient_name}")
    print(f"Доктор: {doctor.doctor_name}")
