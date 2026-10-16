"""ЛАБОРАТОРНА 7. Стек і черга"""
from collections import deque
from dataclasses import dataclass

lines = [                             # вхід для задачі 1
    "",
    "a + b",
    "{[a] + (b)}",
    "([)]",
    "a)",
    "(a[b]",
    "f(x[1]) * {y + (z)}",
]


@dataclass
class Request:
    name: str
    minutes: int                      # скільки хвилин триває обробка


requests = [                          # вхід для задачі 2
    Request("Довідка про навчання", 4),
    Request("Академічна відпустка", 7),
    Request("Копія наказу", 2),
    Request("Виписка з оцінками", 6),
    Request("Перескладання", 9),
    Request("Студентський квиток", 3),
]

PAIRS = {")": "(", "]": "[", "}": "{"}


def is_balanced(line):
    """TODO 1: true, якщо дужки в рядку розставлені правильно."""
    stack = []                        # готовий стек: list (append / pop)
    for ch in line:
        if ch in "([{":
            stack.append(ch)
        elif ch in PAIRS:
            if not stack:             # перевірка на порожність перед pop
                return False          # закривна дужка без відкривної
            if stack.pop() != PAIRS[ch]:
                return False          # пари перетинаються: ([)]
    return not stack                  # у стеку щось лишилось -> не закрили


def process_queue(requests):
    """TODO 2: обробити заявки в порядку надходження, повернути загальний час."""
    queue = deque(requests)           # готова черга: collections.deque
    if not queue:
        print("Заявок немає, обробляти нічого.")
        return 0

    time = 0
    done = 0
    total_wait = 0
    while queue:                      # перевірка на порожність перед popleft
        req = queue.popleft()
        start, end = time, time + req.minutes
        done += 1
        total_wait += start           # усі заявки надійшли в хвилину 0
        print(f"{done}. {req.name:<24} з {start} до {end} хв")
        time = end

    print(f"Оброблено заявок: {done}, загальний час: {time} хв")
    print(f"Середній час очікування: {total_wait / done:.1f} хв")
    return time


def main():
    print("=== Задача 1. Перевірка дужок ===")
    good = 0
    for line in lines:
        ok = is_balanced(line)
        good += ok
        shown = line if line else "(порожній рядок)"
        print(f"{shown:<22} -> {'так' if ok else 'ні'}")
    print(f"Збалансованих рядків: {good}")

    print("\n=== Задача 2. Обробка заявок ===")
    process_queue(requests)

    print("\n=== Порожня черга ===")
    process_queue([])


if __name__ == "__main__":
    main()
