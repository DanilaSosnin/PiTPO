def game_winner(n):
    turn = 0  # 0 - ход Стэна, 1 - ход Олли
    p = 1

    while p < n:
        if turn == 0:  # Стэн делает ход
            p *= 9  # Стэн всегда умножает на 9 для максимального увеличения
        else:  # Олли делает ход
            p *= 8  # Олли будет умножать на 8
        turn = 1 - turn  # Меняем ход

    return "Stan wins" if turn == 1 else "Ollie wins"  # Если после выхода из цикла ход был у Стэна, значит Стэн победил


def main():
    print("Введите числа для игр, каждое на новой строке (для завершения введите пустую строку):")
    results = []

    while True:
        n = input().strip()  # Считываем строку
        if n == "":  # Пустая строка - конец ввода
            break
        try:
            n = int(n)
            results.append(game_winner(n))  # Добавляем результат игры в список
        except ValueError:
            print("Введите корректное число!")

    print("Результат:")
    for result in results:
        print(result)  # Печатаем результаты всех игр


if __name__ == "__main__":
    main()
