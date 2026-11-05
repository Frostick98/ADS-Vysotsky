# ЛАБОРАТОРНА 11. Обхід дерева
# Дерево не змінювати. Готових бібліотек для роботи з деревами не брати —
# обхід писати самостійно.


class Node:
    def __init__(self, title, children):
        self.title = title
        self.children = children


menu = Node("Головне меню", [
    Node("Файл",    [Node("Новий", []), Node("Зберегти", [])]),
    Node("Правка",  [Node("Копіювати", [])]),
    Node("Вигляд",  [Node("Масштаб", [Node("Збільшити", []), Node("Зменшити", [])])]),
    Node("Довідка", []),
])

call_count = 0  # лічильник викликів, збільшується на початку count_items


# 1. Вивести всю ієрархію з відступом за рівнем вкладеності
def print_menu(node, level=0):
    print("  " * level + node.title)
    for child in node.children:
        print_menu(child, level + 1)


# 2. Повернути кількість усіх пунктів меню, враховуючи сам вузол
def count_items(node):
    global call_count
    call_count += 1
    return 1 + sum(count_items(child) for child in node.children)


# 3. Повернути True, якщо в дереві є пункт із такою назвою
def find(node, name):
    return node.title == name or any(find(child, name) for child in node.children)


if __name__ == "__main__":
    print_menu(menu)
    print()
    print("count_items(menu) =", count_items(menu))
    print("викликів count_items =", call_count)
    for name in ("Зберегти", "Масштаб", "Довідка", "Експорт"):
        print(f'find(menu, "{name}") =', find(menu, name))
