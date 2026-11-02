# ЛАБОРАТОРНА 10. Пріоритетні задачі
# Мова: Python 3. Черга з пріоритетом: модуль heapq зі стандартної бібліотеки
# (heappush / heappop). Це мін-купа: першим виходить НАЙМЕНШЕ значення ключа,
# тому окремо перевертати порядок не потрібно: 1 (критично) вийде першим.

import heapq
from dataclasses import dataclass


@dataclass
class Request:
    name: str
    priority: int   # 1 — критично, 2 — важливо, 3 — може почекати
    seq: int        # порядковий номер надходження

    # Для задачі 1: заявки порівнюються ЛИШЕ за пріоритетом (seq ігнорується).
    def __lt__(self, other):
        return self.priority < other.priority


incoming = [  # у порядку надходження
    Request("Оновити підпис у листі",    3, 1),
    Request("Сервер не відповідає",      1, 2),
    Request("Не друкує принтер",         2, 3),
    Request("Не працює термінал оплати", 1, 4),
    Request("Змінити шпалери",           3, 5),
]

late = Request("Відвалився інтернет у відділі", 1, 6)  # для задачі 3


def show(n, r):
    print(f"{n}. {r.name} (пріоритет {r.priority}, seq {r.seq})")


# Задача 1. Ключ — тільки пріоритет.
def processAll(incoming):
    heap = []
    for r in incoming:
        heapq.heappush(heap, r)          # порівнюється Request.__lt__ -> priority
    n = 0
    while heap:
        n += 1
        show(n, heapq.heappop(heap))


# Задача 2. Ключ — пара (priority, seq). seq унікальний, тож Request
# між собою порівнювати вже ніколи не доводиться.
def processStable(incoming):
    heap = []
    for r in incoming:
        heapq.heappush(heap, (r.priority, r.seq, r))
    n = 0
    while heap:
        n += 1
        _, _, r = heapq.heappop(heap)
        show(n, r)


# Задача 3. Дві заявки обробляємо, потім надходить late, і далі до кінця.
def processWithLate(incoming, late):
    heap = []
    for r in incoming:
        heapq.heappush(heap, (r.priority, r.seq, r))
    n = 0
    for _ in range(2):
        n += 1
        _, _, r = heapq.heappop(heap)
        show(n, r)
    heapq.heappush(heap, (late.priority, late.seq, late))   # надійшла посеред обробки
    while heap:
        n += 1
        _, _, r = heapq.heappop(heap)
        show(n, r)


if __name__ == "__main__":
    print("--- Задача 1 ---")
    processAll(incoming)
    print("--- Задача 2 ---")
    processStable(incoming)
    print("--- Задача 3 ---")
    processWithLate(incoming, late)


# ---- Вивід програми ----
# --- Задача 1 ---
# 1. Сервер не відповідає (пріоритет 1, seq 2)
# 2. Не працює термінал оплати (пріоритет 1, seq 4)
# 3. Не друкує принтер (пріоритет 2, seq 3)
# 4. Оновити підпис у листі (пріоритет 3, seq 1)
# 5. Змінити шпалери (пріоритет 3, seq 5)
# --- Задача 2 ---
# 1. Сервер не відповідає (пріоритет 1, seq 2)
# 2. Не працює термінал оплати (пріоритет 1, seq 4)
# 3. Не друкує принтер (пріоритет 2, seq 3)
# 4. Оновити підпис у листі (пріоритет 3, seq 1)
# 5. Змінити шпалери (пріоритет 3, seq 5)
# --- Задача 3 ---
# 1. Сервер не відповідає (пріоритет 1, seq 2)
# 2. Не працює термінал оплати (пріоритет 1, seq 4)
# 3. Відвалився інтернет у відділі (пріоритет 1, seq 6)
# 4. Не друкує принтер (пріоритет 2, seq 3)
# 5. Оновити підпис у листі (пріоритет 3, seq 1)
# 6. Змінити шпалери (пріоритет 3, seq 5)
