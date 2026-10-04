# ЛАБОРАТОРНА 5. Сортування об'єктів
from dataclasses import dataclass


@dataclass
class Student:
    surname: str
    group: str
    grade: int   # середній бал
    year: int    # рік вступу


students = [
    Student("Ткаченко",  "ІПЗ-3/1", 85, 2024),
    Student("Бондар",    "ІПЗ-3/2", 92, 2023),
    Student("Іваненко",  "ІПЗ-3/1", 85, 2024),
    Student("Коваль",    "ІПЗ-3/2", 78, 2024),
    Student("Сидоренко", "ІПЗ-3/1", 85, 2023),
    Student("Мельник",   "ІПЗ-3/2", 92, 2024),
    Student("Гриценко",  "ІПЗ-3/1", 78, 2023),
    Student("Дяченко",   "ІПЗ-3/2", 85, 2023),
]


def print_all(title, items):  # готово, не змінювати
    print(title)
    for s in items:
        print(s.surname, s.group, s.grade, s.year)
    print()


# Українська абетка. Звичайне порівняння рядків іде за кодами Юнікоду,
# де «І» (U+0406) стоїть раніше за «А», тому потрібен свій ключ.
ALPHABET = "абвгґдеєжзиіїйклмнопрстуфхцчшщьюя"
ORDER = {ch: i for i, ch in enumerate(ALPHABET)}


def alpha_key(text):
    return [ORDER.get(ch, len(ALPHABET)) for ch in text.lower()]


# TODO 1: за прізвищем, за абеткою
# sorted() повертає НОВИЙ список, вихідний students не змінюється
by_surname = sorted(students, key=lambda s: alpha_key(s.surname))

# TODO 2: за балом, від вищого до нижчого
by_grade = sorted(students, key=lambda s: s.grade, reverse=True)

# TODO 3: за групою, а всередині групи — за балом від вищого
# Головний ключ — група, другий — бал (зі знаком мінус для спадання)
by_group_grade = sorted(students, key=lambda s: (s.group, -s.grade))

# Частина 2: однакові бали — прізвища за абеткою.
# Ключ-кортеж: спочатку бал (спадання), потім прізвище.
by_grade_then_surname = sorted(students, key=lambda s: (-s.grade, alpha_key(s.surname)))

if __name__ == "__main__":
    print_all("Вихідний список", students)
    print_all("1. За прізвищем", by_surname)
    print_all("2. За балом (від вищого)", by_grade)
    print_all("3. За групою, всередині — за балом (від вищого)", by_group_grade)
    print_all("Частина 2: бал (від вищого), при рівних — прізвище за абеткою",
              by_grade_then_surname)
