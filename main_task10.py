import heapq
from collections import defaultdict


# Алгоритм Дейкстры для нахождения кратчайших путей от нескольких источников
def dijkstra(start_nodes, num_intersections, graph):
    dist = [float('inf')] * (num_intersections + 1)
    pq = []

    # Для всех существующих депо
    for node in start_nodes:
        dist[node] = 0
        heapq.heappush(pq, (0, node))

    while pq:
        d, node = heapq.heappop(pq)

        if d > dist[node]:
            continue

        for neighbor, weight in graph[node]:
            new_dist = dist[node] + weight
            if new_dist < dist[neighbor]:
                dist[neighbor] = new_dist
                heapq.heappush(pq, (new_dist, neighbor))

    return dist


def solve():
    t = int(input("Введите количество тестов: "))  # количество тестов
    input()  # пустая строка перед первым тестом

    for test_case in range(1, t + 1):
        print(f"Тест #{test_case}:")

        # Вводим данные для каждого теста
        print("Введите количество пожарных депо и перекрестков:")
        f, i = map(int, input().split())

        fire_stations = []

        print("Введите номера перекрестков с пожарными депо:")
        for _ in range(f):
            fire_stations.append(int(input()))

        graph = defaultdict(list)

        print("Введите данные о дорогах (номер1 номер2 длина):")
        while True:
            line = input().strip()
            if not line:
                break
            u, v, w = map(int, line.split())
            graph[u].append((v, w))
            graph[v].append((u, w))

        # Получаем минимальные расстояния от всех существующих депо
        dist_from_depos = dijkstra(fire_stations, i, graph)

        # Теперь находим оптимальный перекресток для нового депо
        best_intersection = -1
        best_distance = float('inf')

        # Перебираем все перекрестки и проверяем, на каком новом депо минимальное максимальное расстояние
        for new_depot in range(1, i + 1):
            # Модифицируем граф, чтобы добавить новое депо
            dist_from_new_depot = dist_from_depos[:]
            dist_from_new_depot = dijkstra([new_depot], i, graph)

            # Находим максимальное расстояние от любого перекрестка до ближайшего депо
            max_dist = max(dist_from_new_depot[1:])

            # Если нашли меньший максимум, обновляем лучший результат
            if max_dist < best_distance:
                best_distance = max_dist
                best_intersection = new_depot

        print(f"Результат:")
        print(best_intersection)
        print()


if __name__ == "__main__":
    solve()
