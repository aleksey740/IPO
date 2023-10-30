class WaterResources:
    """
    Класс для описания информации о водных ресурсах.
    Атрибуты:
    - name (str): Название водного ресурса.
    - location (str): Местоположение водного ресурса.
    - capacity (float): Общая вместимость водного ресурса.
    - current_level (float): Текущий уровень воды.
    - usage (str): Назначение водного ресурса.

    Методы:
    - calculate_available_capacity(self): Рассчитывает доступную вместимость водного ресурса.
    - use_water(self, amount): Использует указанное количество воды из ресурса.
    - refill_water(self, amount): Пополняет водный ресурс на указанное количество.
    - water_level_percentage(self): Возвращает процент заполнения водного ресурса.
    """
    def __init__(self, name, location, capacity, current_level, usage):
        self.name = name
        self.location = location
        self.capacity = capacity
        self.current_level = current_level
        self.usage = usage
    def calculate_available_capacity(self):
        return self.capacity - self.current_level
    def use_water(self, amount):
        if amount <= self.current_level:
            self.current_level -= amount
            return f"{amount} млн. куб. м воды извлечено из {self.name}."
        else:
            return f"Недостаточно воды в {self.name} для запрошенного количества."
    def refill_water(self, amount):
        self.current_level += amount
        return f"{amount} млн. куб. м воды добавлено в {self.name}."
    def water_level_percentage(self):
        percentage = (self.current_level / self.capacity) * 100
        return f"Заполнено на {percentage:.2f}%"

#использование класса WaterResources
if __name__ == "__main__":
    #ввывод документацию класса:
    print(WaterResources.__doc__)

    #Создание экземпляров класса
    river = WaterResources("Река Ошмянка", "Беларусь", 2000, 1500, "-")
    lake = WaterResources("Озеро Меловой карьер", "Беларусь", 23620, 15000, "Природоохранное")
    reservoir = WaterResources("Водохранилище Вилейское", "Беларусь", 1000, 700, "Промышленное")
    well = WaterResources("Скважина", "Сельское хозяйство", 50, 40, "Сельское хозяйство")
    spring = WaterResources("Источник Боровой", "Беларусь", 10, 5, "Питьевая")

    #вывод метода класса
    print(river.use_water(100))
    print(lake.refill_water(200))
    print(reservoir.calculate_available_capacity())
    print(well.water_level_percentage())
