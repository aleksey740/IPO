class Pet: #Создание класса Pet
    def __init__(self, name, age, breed, weight):
        self._name = name #Инициализация свойства имени
        self._age = age #Инициализация свойства возраста
        self._breed = breed #Инициализация свойства породы
        self._weight = weight #Инициализация свойства веса

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if not isinstance(new_name, str):
            raise ValueError("Имя должно быть строкой") #Проверка, если имя не является строкой
        self._name = new_name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, new_age):
        if not isinstance(new_age, int) or new_age < 0:
            raise ValueError("Возраст должен быть неотрицательным целым числом") #Проверка, если возраст не является неотрицательным целым числом
        self._age = new_age

    @property
    def breed(self):
        return self._breed

    @breed.setter
    def breed(self, new_breed):
        if not isinstance(new_breed, str):
            raise ValueError("Порода должна быть строкой") #Проверка, если порода не является строкой
        self._breed = new_breed

    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, new_weight):
        if not isinstance(new_weight, (int, float)) or new_weight <= 0:
            raise ValueError("Вес должен быть положительным числом") #Проверка, если вес не является положительным числом
        self._weight = new_weight

#Пример использования класса
if __name__ == "__main__":
    #Создание объекта с использованием конструктора
    my_pet = Pet(name="Рэм", age=4, breed="Собака", weight=8.6)

    # Использование геттеров
    print(f"Имя: {my_pet.name}")
    #Используем условие для выбора формы слова год или лет в зависимости от числа
    print(f"Возраст: {my_pet.age} {'лет' if my_pet.age == 1 else 'года'}")
    print(f"Вид: {my_pet.breed}")
    print(f"Вес: {my_pet.weight} кг")

    #Использование сеттеров
    my_pet.name = "Ричард"
    my_pet.age = 2
    my_pet.breed = "Dog"
    my_pet.weight = 4.5

    print(f"\nИмя: {my_pet.name}")
    print(f"Возраст: {my_pet.age} {'лет' if my_pet.age == 1 else 'года'}")
    print(f"Вид: {my_pet.breed}")
    print(f"Вес: {my_pet.weight} кг")

    try: #Попытка изменения значения напрямую (вызов ошибки)
        my_pet.age = -1  #вызов ValueError из сеттера
    except ValueError as e:
        print(f"\nОшибка: {e}")
