# ЛАБОРАТОРНА 8. Швидкий пошук ключів
# Дані не змінювати. Міняти тільки код фрагментів.

from collections import namedtuple

Client = namedtuple("Client", ["id", "name"])
Order = namedtuple("Order", ["number", "client_id", "sum"])

clients = [  # id, прізвище
    Client(101, "Коваленко"),
    Client(102, "Мельник"),
    Client(103, "Шевчук"),
    Client(104, "Бондар"),
    Client(105, "Ткачук"),
    Client(106, "Гриценко"),
]

orders = [  # номер, id клієнта, сума
    Order(1, 103, 450), Order(2, 101, 120),
    Order(3, 105, 980), Order(4, 103, 300),
    Order(5, 102, 75),  Order(6, 106, 1500),
    Order(7, 101, 220), Order(8, 103, 60),
]

blocked = [102, 104]  # заблоковані клієнти


# ---------------------------------------------------------------
# Фрагмент 1. Ім'я клієнта для кожного замовлення
# Було: для кожного замовлення — повний прохід по списку клієнтів.
# Стало: словник «id клієнта -> клієнт», побудований один раз.
# ---------------------------------------------------------------
print("--- Фрагмент 1 ---")

# # СТАРИЙ ВАРІАНТ
# for order in orders:
#     for client in clients:
#         if client.id == order.client_id:
#             print("Замовлення " + str(order.number) + " — " + client.name)

# НОВИЙ ВАРІАНТ
client_by_id = {}
for client in clients:
    client_by_id[client.id] = client

for order in orders:
    print("Замовлення " + str(order.number) + " — " + client_by_id[order.client_id].name)


# ---------------------------------------------------------------
# Фрагмент 2. Сума замовлень, крім заблокованих клієнтів
# Було: blocked — список, `in` шукає перебором для кожного замовлення.
# Стало: множина set заблокованих id.
# ---------------------------------------------------------------
print("--- Фрагмент 2 ---")

# # СТАРИЙ ВАРІАНТ
# total = 0
# for order in orders:
#     if order.client_id not in blocked:
#         total = total + order.sum
# print("Сума прийнятих замовлень: " + str(total))

# НОВИЙ ВАРІАНТ
blocked_set = set(blocked)
total = 0
for order in orders:
    if order.client_id not in blocked_set:
        total = total + order.sum
print("Сума прийнятих замовлень: " + str(total))


# ---------------------------------------------------------------
# Фрагмент 3. Скільки замовлень у кожного клієнта
# Було: список counted + вкладений прохід по всіх замовленнях.
# Стало: словник «id клієнта -> лічильник» за один прохід;
#        порядок виводу задає список first_seen (порядок першої появи).
# ---------------------------------------------------------------
print("--- Фрагмент 3 ---")

# # СТАРИЙ ВАРІАНТ
# counted = []
# for order in orders:
#     if order.client_id in counted:
#         continue
#     count = 0
#     for other in orders:
#         if other.client_id == order.client_id:
#             count = count + 1
#     counted.append(order.client_id)
#     print(str(order.client_id) + ": " + str(count))

# НОВИЙ ВАРІАНТ
counts = {}
first_seen = []
for order in orders:
    if order.client_id in counts:
        counts[order.client_id] += 1
    else:
        counts[order.client_id] = 1
        first_seen.append(order.client_id)

for client_id in first_seen:
    print(str(client_id) + ": " + str(counts[client_id]))


# ---------------------------------------------------------------
# Фрагмент 4. Найбільше замовлення
# НЕ ЗМІНЮВАВ: один прохід, пошуку за ключем немає.
# ---------------------------------------------------------------
print("--- Фрагмент 4 ---")

best = orders[0]
for order in orders:
    if order.sum > best.sum:
        best = order
print("Найбільше замовлення: " + str(best.sum))


# ---------------------------------------------------------------
# Фрагмент 5. Чийсь «оптимізований» варіант фрагмента 1
# НЕ ЗМІНЮВАВ: словник уже є, але створюється всередині циклу
# (для кожного замовлення заново), тому виграшу немає.
# ---------------------------------------------------------------
print("--- Фрагмент 5 ---")

for order in orders:
    by_id = {}
    for client in clients:
        by_id[client.id] = client
    print("Замовлення " + str(order.number) + " — " + by_id[order.client_id].name)
