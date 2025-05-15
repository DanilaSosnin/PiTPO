def find_longest_sequence(slon):
    n = len(slon)
    dp = [1] * n  # Массив для хранения длины последовательности для каждого слона
    parent = [-1] * n  # Массив для восстановления последовательности

    # Заполнение массива dp
    for i in range(1, n):
        for j in range(i):
            # Проверяем, если вес слона i больше веса слона j и IQ слона i меньше IQ слона j
            if slon[i][0] > slon[j][0] and slon[i][1] < slon[j][1]:
                if dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
                    parent[i] = j

    # Находим индекс самого длинного пути
    max_len = max(dp)
    index = dp.index(max_len)

    # Восстанавливаем последовательность
    sequence = []
    while index != -1:
        sequence.append(index)
        index = parent[index]

    sequence.reverse()  # Переворачиваем последовательность, так как мы восстанавливаем её с конца
    return max_len, sequence


def solve():
    print("Введите данные слонов (вес и IQ через пробел):")
    slon = []

    # Чтение данных слонов
    while True:
        try:
            line = input()
            if not line:  # Если строка пустая, завершить ввод
                break
            weight, iq = map(int, line.split())  # Вводим вес и IQ каждого слона
            slon.append((weight, iq))
        except ValueError:
            print("Пожалуйста, введите два целых числа для каждого слона.")
            continue

    # Находим результат для данной последовательности
    result_len, sequence = find_longest_sequence(slon)

    # Выводим результат
    print("Результат:")
    print(result_len)
    for index in sequence:
        print(index + 1)  # Печатаем номер слона (индекс + 1), а не индекс


if __name__ == "__main__":
    solve()
