# ЛАБОРАТОРНА 12. Просте BST
# Набір чисел і порядок вставки не змінювати.
# Готових впорядкованих колекцій не беремо — дерево будуємо самі.


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None    # порожньо, якщо нащадка немає
        self.right = None


root = None

values = [42, 18, 65, 9, 27, 55, 90, 33]  # вставляти саме в цьому порядку

compare_count = 0  # лічильник порівнянь, збільшується на початку кожного порівняння в search


def insert(node, key):
    """Вставляє число в дерево й повертає корінь піддерева.
    Якщо число вже є — дерево не змінюється."""
    if node is None:                      # базовий випадок: порожнє місце -> новий листок
        return Node(key)
    if key < node.value:
        node.left = insert(node.left, key)
    elif key > node.value:
        node.right = insert(node.right, key)
    # key == node.value: дублікат, нічого не робимо
    return node


def search(node, key):
    """Повертає True, якщо число є в дереві. Рахує порівняння."""
    global compare_count
    if node is None:                      # дійшли до порожнього місця — числа немає
        return False
    compare_count += 1                    # порівняння ключа з вузлом
    if key == node.value:
        return True
    if key < node.value:
        return search(node.left, key)
    return search(node.right, key)


def inorder(node, result=None):
    """Симетричний обхід: ліве піддерево -> вузол -> праве піддерево."""
    if result is None:
        result = []
    if node is not None:
        inorder(node.left, result)
        result.append(node.value)
        inorder(node.right, result)
    return result


def count_nodes(node):
    if node is None:
        return 0
    return 1 + count_nodes(node.left) + count_nodes(node.right)


def height(node):
    """Глибина найдовшої гілки в вузлах (порожнє дерево = 0)."""
    if node is None:
        return 0
    return 1 + max(height(node.left), height(node.right))


def run_search(key):
    """Обнуляє лічильник, шукає key, повертає (знайдено, порівнянь)."""
    global compare_count
    compare_count = 0
    found = search(root, key)
    return found, compare_count


if __name__ == "__main__":
    for v in values:
        root = insert(root, v)

    print("Вузлів у дереві після восьми вставок:", count_nodes(root))
    print("Симетричний обхід:", " ".join(map(str, inorder(root))))

    found, cnt = run_search(55)
    print("search(root, 55):", "так" if found else "ні")
    print("Порівнянь під час пошуку 55:", cnt)

    found, cnt = run_search(30)
    print("search(root, 30):", "так" if found else "ні")
    print("Порівнянь під час пошуку 30:", cnt)

    print("Глибина найдовшої гілки:", height(root))

    root = insert(root, 27)
    print("Вузлів після повторної вставки числа 27:", count_nodes(root))
