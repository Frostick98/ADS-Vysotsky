"""
Задача 3. Останні N подій.

Зберігаємо лише N останніх подій у масиві фіксованого розміру N (кільцевий буфер).
Найстаріша подія ніколи не видаляється зсувом з початку колекції — замість цього
запис просто перезаписується в комірці, на яку вказує лічильник наступного запису.
"""


class LastNEvents:
    def __init__(self, capacity):
        self._capacity = capacity
        self._buffer = [None] * capacity   # масив на N позицій
        self._next_slot = 0                # комірка, у яку писати наступного разу
        self._count = 0                    # скільки реальних подій уже записано

    def add(self, event):
        self._buffer[self._next_slot] = event
        self._next_slot = (self._next_slot + 1) % self._capacity  # по колу з нуля
        self._count = min(self._count + 1, self._capacity)

    def oldest_to_newest(self):
        """Повертає збережені події від найстарішої до найновішої."""
        if self._count < self._capacity:
            # буфер ще не заповнився повністю — записи від 0 до count-1 і є порядком
            return self._buffer[:self._count]

        # буфер заповнений: найстаріший запис лежить саме на _next_slot
        return self._buffer[self._next_slot:] + self._buffer[:self._next_slot]


def main():
    N = 5
    recent = LastNEvents(N)

    incoming_events = [
        "подія №1", "подія №2", "подія №3", "подія №4",
        "подія №5", "подія №6", "подія №7", "подія №8",
    ]

    for event in incoming_events:
        recent.add(event)
        print(f"Надійшла {event}")

    print(f"\nОстанні {N} подій (від найстарішої до найновішої):")
    for event in recent.oldest_to_newest():
        print(f"  {event}")


if __name__ == "__main__":
    main()
