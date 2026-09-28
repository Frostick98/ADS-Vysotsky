# ЛАБОРАТОРНА 4. Пошук у даних

data = [42, 8, 60, 19, 3, 55, 12, 31, 68, 24, 49, 37, 71, 5, 27]
sorted_data = sorted(data)          # готово

comparisons = 0                     # лічильник порівнянь, обнуляється перед кожним пошуком


def linear_search(items, target):
    """Повертає індекс знайденого значення або -1."""
    global comparisons
    for i in range(len(items)):
        comparisons += 1            # порівняння items[i] з target
        if items[i] == target:
            return i
    return -1


def binary_search(items, target):
    """Повертає індекс знайденого значення або -1. Працює лише на відсортованих даних."""
    global comparisons
    low, high = 0, len(items) - 1
    while low <= high:
        mid = low + (high - low) // 2
        comparisons += 1            # порівняння items[mid] з target
        if items[mid] == target:
            return mid
        elif items[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1


def report(name, items, target):
    global comparisons
    comparisons = 0
    index = linear_search(items, target) if name == "linear" else binary_search(items, target)
    print(name, target, index, comparisons)
    return index, comparisons


if __name__ == "__main__":
    cases = [
        (sorted_data, 3), (sorted_data, 71), (sorted_data, 31),
        (sorted_data, 1), (sorted_data, 99), (sorted_data, 50),
        ([42], 42), ([], 42),
    ]
    for n, (items, target) in enumerate(cases, 1):
        print("Випадок", n)
        report("linear", items, target)
        report("binary", items, target)

    print("Експеримент: бінарний пошук на невідсортованому data, шукаємо 55")
    report("binary", data, 55)
