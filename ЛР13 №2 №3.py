class Rub(object):
    """ Класс для работы с рублями и копейками."""
    def __init__(self, rub=0, kop=0):
        self.rub = rub
        self.kop = kop
        self.normalize()

    def normalize(self):
        """Нормализация значений: перевод копеек в рубли, оставляя остаток в копейках."""
        self.rub += self.kop // 100
        self.kop %= 100

    def __str__(self):
        """Строковое представление объекта Rub."""
        return f"{self.rub:02d}.{self.kop:02d} rub"

    def __lt__(self, other):
        """Метод для сравнения объектов Rub."""
        if self.rub == other.rub:
            return self.kop < other.kop
        return self.rub < other.rub

    def __add__(self, other):
        """Метод для сложения объектов Rub."""
        res = Rub(self.rub + other.rub, self.kop + other.kop)
        res.normalize()
        return res

class Goods(object):
    """ Класс описания товара: название и цена"""
    def __init__(self, name='', rub=0, kop=0):
        self.name = name
        self.price = Rub(rub, kop)

    def __str__(self):
        """Строковое представление объекта Goods."""
        return f"{self.name} {self.price}"

def process_order(goods_list):
    """Обработка заказа: вывод отсортированного списка товаров, подсчет общей стоимости и сдачи."""
    goods_list.sort(key=lambda x: x.price, reverse=True)

    total = Rub()
    for item in goods_list:
        print(item)
        total += item.price

    print(f"\ntotal {total}")

    amount_paid = input("Сколько денег вы дали? ")
    amount_paid = Rub(*map(int, amount_paid.split('.')))

    change = amount_paid - total
    print(f"change {change}")

# Пример использования:

order1 = [Goods("rice", 10, 50), Goods("tea", 6, 30), Goods("cake", 10, 12), Goods("salad", 20, 0)]
process_order(order1)

order2 = [Goods("tender", 100, 0)]
process_order(order2)
