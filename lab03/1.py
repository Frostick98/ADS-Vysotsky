"""
Задача 1. Журнал у зворотному порядку.

Складаємо рядки у динамічний список лише додаванням у кінець (append),
а порядок змінюємо вже після того, як усе зібрано — вставка на початок
(insert(0, ...)) ніде не використовується.
"""


def build_journal(raw_lines):
    """Складає динамічний список, додаючи елементи тільки в кінець."""
    journal = []
    for line in raw_lines:
        journal.append(line)
    return journal


def reversed_journal(journal):
    """Повертає новий список у зворотному порядку (без insert(0, ...))."""
    return journal[::-1]


def main():
    raw_lines = [
        "10:01 INFO  Сервіс запущено",
        "10:02 DEBUG Підключення до бази даних",
        "10:05 WARN  Повільна відповідь від API",
        "10:07 INFO  Користувач увійшов у систему",
        "10:09 ERROR Не вдалося зберегти файл",
    ]

    journal = build_journal(raw_lines)

    print("Журнал у прямому порядку:")
    for entry in journal:
        print(f"  {entry}")

    print("\nЖурнал у зворотному порядку:")
    for entry in reversed_journal(journal):
        print(f"  {entry}")


if __name__ == "__main__":
    main()
