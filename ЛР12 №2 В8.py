class WaterResources:
    """
    Класс для описания информации о водных ресурсах.
    Методы:
    - calculate_available_capacity(self): Рассчитывает доступную вместимость водного ресурса.
    - use_water(self, amount): Использует указанное количество воды из ресурса.
    - refill_water(self, amount): Пополняет водный ресурс на указанное количество.
    - water_level_percentage(self): Возвращает процент заполнения водного ресурса.
    """

    def __init__(self):
        #Конструктор класса, инициализирует атрибуты объекта
        self.name = None
        self.location = None
        self.capacity = None
        self.current_level = None
        self.usage = None

    def set_attributes(self, name, location, capacity, current_level, usage):
        #Метод для установки значений атрибутов объекта
        self.name = name
        self.location = location
        self.capacity = capacity
        self.current_level = current_level
        self.usage = usage

    def calculate_available_capacity(self):
        #Метод для расчета доступной вместимости водного ресурса
        return self.capacity - self.current_level

    def use_water(self, amount):
        #Метод для использования указанного количества воды из ресурса
        if amount <= self.current_level:
            self.current_level -= amount
            return f"{amount} млн. куб. м воды извлечено из {self.name}."
        else:
            return f"Недостаточно воды в {self.name} для запрошенного количества."

    def refill_water(self, amount):
        #Метод для пополнения водного ресурса указанным количеством воды
        self.current_level += amount
        return f"{amount} млн. куб. м воды добавлено в {self.name}."

    def water_level_percentage(self):
         #Метод для расчета процента заполнения водного ресурса
        percentage = (self.current_level / self.capacity) * 100
        return f"Заполнено на {percentage:.2f}%"

    def __del__(self):
        #Деструктор (финализатор) класса, вызывается при удалении объекта
        print(f"Деструктор вызван для {self.name}")


if __name__ == "__main__":
    water_resources_list = []

    #Запрашиваем данные для 10 экземпляров класса и добавляем их в список
    for _ in range(10):
        resource = WaterResources()
        name = input("Введите название водного ресурса: ")
        location = input("Введите местоположение водного ресурса: ")
        capacity = float(input("Введите общую вместимость водного ресурса: "))
        current_level = float(input("Введите текущий уровень воды: "))
        usage = input("Введите назначение водного ресурса: ")
        resource.set_attributes(name, location, capacity, current_level, usage)
        water_resources_list.append(resource)

    #Убеждаемся, что деструктор вызывается для каждого объекта при завершении программы
    del water_resources_list
