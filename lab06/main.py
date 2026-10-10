# ЛАБОРАТОРНА 6. Рекурсивний обхід


class Category:
    def __init__(self, name, products, children):
        self.name = name
        self.products = products      # товарів безпосередньо в цій категорії
        self.children = children      # список підкатегорій


catalog = Category("Каталог", 0, [
    Category("Одяг", 0, [
        Category("Верхній одяг", 0, [
            Category("Куртки", 12, []),
            Category("Пальта", 7, []),
        ]),
        Category("Светри", 15, []),
    ]),
    Category("Взуття", 4, [
        Category("Кросівки", 23, []),
        Category("Чоботи", 9, []),
    ]),
    Category("Аксесуари", 0, [
        Category("Сумки", 18, []),
        Category("Ремені", 5, []),
    ]),
])

call_count = 0   # лічильник викликів, збільшується на початку кожної функції


def print_tree(node, level):
    global call_count
    call_count += 1
    print("  " * level + node.name)
    for child in node.children:
        print_tree(child, level + 1)           # рівень на 1 більший


def count_products(node):
    global call_count
    call_count += 1
    if not node.children:                      # базовий випадок: категорія без підкатегорій
        return node.products
    total = node.products                      # свої товари + товари кожної підкатегорії
    for child in node.children:
        total += count_products(child)
    return total


def max_depth(node):
    global call_count
    call_count += 1
    if not node.children:                      # базовий випадок: лист має глибину 1
        return 1
    return 1 + max(max_depth(child) for child in node.children)


if __name__ == "__main__":
    call_count = 0
    print_tree(catalog, 0)
    lines = call_count                         # кожен виклик друкує рівно один рядок

    call_count = 0
    total = count_products(catalog)
    count_calls = call_count

    call_count = 0
    depth = max_depth(catalog)

    print()
    print("Рядків у виводі print_tree:", lines)
    print("Товарів у каталозі:", total)
    print("Глибина найдовшої гілки:", depth)
    print("Викликів count_products:", count_calls)
