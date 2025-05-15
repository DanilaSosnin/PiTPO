import itertools

def count_visible_people(perm):
    n = len(perm)
    left_visible = 0
    right_visible = 0

    # Проверка видимости слева
    max_left = -1
    for i in range(n):
        if perm[i] > max_left:
            left_visible += 1
            max_left = perm[i]

    # Проверка видимости справа
    max_right = -1
    for i in range(n - 1, -1, -1):
        if perm[i] > max_right:
            right_visible += 1
            max_right = perm[i]

    return left_visible, right_visible


def solve():
    # Пояснение для пользователя
    print("Введите количество тестов:")
    t = int(input())  # Читаем количество тестов
    print("Введите для каждого теста значения N (количество людей), P (количество видящих слева) и R (количество видящих справа):")

    results = []  # Список для хранения результатов

    for _ in range(t):
        N, P, R = map(int, input().split())  # Читаем N, P, R для каждого теста
        count = 0

        # Генерация всех перестановок для N людей
        for perm in itertools.permutations(range(1, N + 1)):
            left_visible, right_visible = count_visible_people(perm)
            if left_visible == P and right_visible == R:
                count += 1

        results.append(str(count))  # Добавляем результат в список

    # Выводим "Результат" только один раз перед всеми результатами
    print("Результат:")
    print("\n".join(results))  # Печатаем все результаты через новую строку


if __name__ == "__main__":
    solve()
