from math import comb

def max_parts(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return 1 + comb(n, 2) + comb(n, 4)


def main():
    print("Введите количество тестов и затем числа для каждого теста:")
    s = int(input())  # Считываем количество тестов
    results = []

    for _ in range(s):
        n = int(input())  # Считываем значение n для каждого случая
        results.append(str(max_parts(n)))  # Добавляем результат в список

    print("\nРезультат:")
    print("\n".join(results))  # Печатаем все результаты


if __name__ == "__main__":
    main()
