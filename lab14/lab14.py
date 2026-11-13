"""Лабораторна робота №14. Досяжність у графі (обхід у ширину, BFS)."""

from collections import deque

# ─── ГОТОВО: модель графа. Нічого тут не змінюємо ──────────────
graph = {}

graph["Центр"] = ["Парк", "Ринок"]
graph["Парк"] = ["Центр", "Вокзал"]
graph["Ринок"] = ["Центр", "Вокзал", "Стадіон"]
graph["Вокзал"] = ["Парк", "Ринок", "Озеро"]
graph["Стадіон"] = ["Ринок"]
graph["Озеро"] = ["Вокзал"]
graph["Гай"] = ["Міст"]
graph["Міст"] = ["Гай"]


# ─── ВАШ КОД ───────────────────────────────────────────────────

def visitAll(graph, start):
    """Обхід у ширину від start. Повертає множину відвіданих вершин."""
    visited = {start}
    queue = deque([start])
    while queue:
        current = queue.popleft()
        for neighbor in graph.get(current, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return visited


def reachable(graph, from_, to):
    """True, якщо з from_ можна дістатися до to; інакше False."""
    return to in visitAll(graph, from_)


def findPath(graph, from_, to):
    """Шлях від from_ до to переліком вершин; порожній список, якщо шляху немає."""
    parent = {from_: None}          # з якої вершини прийшли в кожну
    queue = deque([from_])
    while queue:
        current = queue.popleft()
        for neighbor in graph.get(current, []):
            if neighbor not in parent:
                parent[neighbor] = current
                queue.append(neighbor)

    if to not in parent:            # недосяжна вершина — шляху немає
        return []

    path = []
    node = to
    while node is not None:         # у start позначки немає — кінець
        path.append(node)
        node = parent[node]
    path.reverse()
    return path


# ─── Перевірка (відповідає контрольній таблиці) ────────────────
if __name__ == "__main__":
    print("visitAll('Центр'):", sorted(visitAll(graph, "Центр")))
    print("Кількість вершин:", len(visitAll(graph, "Центр")))
    print("reachable('Центр', 'Озеро'):", reachable(graph, "Центр", "Озеро"))
    print("reachable('Центр', 'Гай'):", reachable(graph, "Центр", "Гай"))
    print("reachable('Гай', 'Міст'):", reachable(graph, "Гай", "Міст"))

    p1 = findPath(graph, "Центр", "Озеро")
    print("findPath('Центр', 'Озеро'):", p1, "ребер:", len(p1) - 1)
    p2 = findPath(graph, "Центр", "Стадіон")
    print("findPath('Центр', 'Стадіон'):", p2, "ребер:", len(p2) - 1)
    print("findPath('Центр', 'Міст'):", findPath(graph, "Центр", "Міст"))
    print("Недосяжні з 'Центру':", len(graph) - len(visitAll(graph, "Центр")))
