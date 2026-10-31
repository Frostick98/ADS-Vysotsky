# ЛАБОРАТОРНА 9. Ключі хеш-колекцій
# Стан "ДО виправлення": рівність визначена за артикулом, хеш — типовий (за адресою об'єкта).
# Примітка: у Python, якщо визначити лише __eq__, мова сама ставить __hash__ = None
# (об'єкт стає нехешованим і set.add дає TypeError). Щоб відтворити вихідний стан із бланка
# (рівність є, хеш типовий), типовий хеш вказано явно.


class Product:
    def __init__(self, code: str, name: str):
        self.code = code    # артикул — саме він визначає товар
        self.name = name    # назва, може змінитися при перейменуванні

    def __eq__(self, other):            # два товари однакові, якщо однаковий артикул
        return isinstance(other, Product) and self.code == other.code

    __hash__ = object.__hash__          # типовий хеш — від ідентичності об'єкта (дефект)

    def __repr__(self):
        return f"Product({self.code!r}, {self.name!r})"


items = [
    Product("A-100", "Кабель USB-C"),
    Product("B-205", "Миша бездротова"),
    Product("A-100", "Кабель USB-C"),
    Product("C-310", "Клавіатура"),
    Product("D-415", "Монітор 24 дюйми"),
    Product("B-205", "Миша бездротова"),
    Product("E-520", "Навушники"),
    Product("F-630", "Вебкамера"),
]

unique = set()
for p in items:
    unique.add(p)                       # мала б лишитися тільки унікальні артикули

stock = {}
stock[Product("A-100", "Кабель USB-C")] = 17
stock[Product("A-100", "Кабель USB-C")] = 25   # той самий артикул, нове число

# Діагностика
a = Product("A-100", "Кабель USB-C")
b = Product("A-100", "Кабель USB-C")

print("(1) a == b              :", a == b)
print("(2) len(unique)         :", len(unique))
print("(3) a in unique         :", a in unique)
print("(4) len(stock)          :", len(stock))
print("(5) a in stock          :", a in stock)

codes = [p.code for p in items]
print("Артикулів, що трапляються двічі:", sum(1 for c in set(codes) if codes.count(c) == 2))
